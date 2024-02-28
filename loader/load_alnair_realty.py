import os
from random import choice
import urllib.request
import logging
import traceback

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')

import django

django.setup()

from listings.models import Listing
from realtors.models import Realtor
from developers.models import Developer

import xmltodict as xmltodict
import json
from utils import is_int, is_float


def developer_get_or_add(title_en, title_ru, title_ar, logo, Realtor, Developer):
    realtor_list = Realtor.objects.all()
    realtors_ids = [realtor.id for realtor in realtor_list]
    unknown_developer, created = Developer.objects.get_or_create(slug='unknown',
                                                                 defaults={'title_en': 'The Unknown',
                                                                           'title_ru': 'The Unknown',
                                                                           'title_ar': 'The Unknown',
                                                                           'logo': '/img/unknown.jpeg',
                                                                           'realtor_id': choice(realtors_ids)})

    titles = [title_en, title_ru, title_ar]
    titles = list(filter(None, titles))
    if titles:
        title_en = title_en if title_en else titles[0]
        title_ru = title_ru if title_ru else titles[0]
        title_ar = title_ar if title_ar else titles[0]
        developer, created = Developer.objects.get_or_create(title_en=title_en,
                                                             defaults={'title_en': title_en,
                                                                       'title_ru': title_ru,
                                                                       'title_ar': title_ar,
                                                                       'logo': logo,
                                                                       'realtor_id': choice(realtors_ids)})
    else:
        developer = unknown_developer
    return developer


class Loader:
    url = None

    def __init__(self, url):
        self.url = url

    def request_content(self):
        say_my_name()
        with urllib.request.urlopen(self.url) as f:
            text = f.read().decode('utf-8')
            return text


def say_my_name():
    stack = traceback.extract_stack()
    logging.info('Исполняется функция {}'.format(stack[-2][2]))


class Downloader(Loader):
    FILE_URL = 'https://api.alnair.ae/v1/feed/download/333035345fa2fab400233833bd5f31/rc'
    database_dict = None

    def __init__(self, url=FILE_URL):
        super().__init__(url)

    def request_xml_db_file(self):
        say_my_name()
        content = self.request_content()
        if content:
            self.database_dict = xmltodict.parse(content, xml_attribs=True)
            to_json_keys = [('amenities', 'amenity'),
                            ('districts', 'district'),
                            ('albums', 'album'),
                            ('br_prices', 'br_price'),
                            ('payment_plans', 'payment_plan'),
                            ('stocks', 'stock')]
            for offer in self.database_dict['realty-feed']['offers']:
                for key, child_key in to_json_keys:
                    if isinstance(offer[key], dict):
                        if len(offer[key]) == 1:
                            if isinstance(offer[key][child_key], dict):
                                offer[key] = [offer[key][child_key], ]
                            else:
                                offer[key] = offer[key][child_key]
                        else:
                            offer[key] = [offer[key], ]
            print('ready')
        else:
            self.database_dict = dict()
            self.database_dict['realty-feed'] = dict()
            self.database_dict['realty-feed']['offers'] = []


class DatabaseDownloader(Downloader):
    TOP_TABLE_PREFIX = 'listings_'
    TOP_TABLE_NAME = 'listing'
    sql_for_create_table = dict()
    sql_for_insert_records = dict()
    python_for_insert_records = dict()
    python_for_create_table = dict()
    tables = dict()

    def __init__(self, *args):
        Downloader.__init__(self, *args)

    def get_fields(self, table_name, key, item, table_func):
        say_my_name()
        # возвращает список полей таблицы
        key = key.replace('-', '_')
        if isinstance(item, dict):
            result = []
            for k in item:
                if k != 'id':
                    if len(item) > 1:
                        result += self.get_fields(table_name,
                                                  ((key + '_a_') if key else '') + k,
                                                  item[k],
                                                  table_func)
                    else:
                        result += self.get_fields(table_name, key, item[k], table_func)
            return result
        elif isinstance(item, list):
            # if table_func:
            #     table_func(item[0], table_name=table_name + '_' + key, fk=(f'{table_name}_id', 'INT', None), )
            return (table_name + '_' + key, 'LIST', json.dumps(item)),
        elif is_int(item):
            return (key if key else "value", 'INT', item),
        elif is_float(item):
            return (key if key else "value", 'REAL', item),
        else:
            return (key if key else "value", 'CHAR', item),

    def get_tables(self, item, table_name=TOP_TABLE_NAME, fk=None):
        say_my_name()
        if item:
            fields = []
            if fk:
                fields.append(fk)
            fields += self.get_fields(table_name, '', item, self.get_tables)
            if fields:
                self.tables[table_name] = fields

            if table_name == self.TOP_TABLE_NAME:
                for i, el in enumerate(self.tables[table_name]):
                    field, field_type, item = el
                    if field in ['amenities', 'districts', 'album', 'albums', 'br_prices', 'payment_plans', 'stocks']:
                        self.tables[table_name][i] = ('listing_' + field, field_type, item)

    def make_dict_with_fields_info(self, defined_fields, table_name=TOP_TABLE_NAME):
        say_my_name()
        fields_dict = dict()
        unknown_fields_list = set()
        for field, field_type, item in self.tables[table_name]:
            if field in defined_fields:
                fields_dict[field] = item
            else:
                unknown_fields_list.add(field)
                logging.warning(f'Field [{field}] is not defined in model Listing')
        # print(fields_dict)
        return fields_dict, unknown_fields_list

    def load_data_into_db(self):
        say_my_name()
        data = self.database_dict['realty-feed']['offers']
        all_records = len(data)
        updated_records = 0
        added_records = 0
        unknown_fields = set()
        listing_fields = [f.name for f in Listing._meta.get_fields()]
        realtor_list = Realtor.objects.all()
        realtors_ids = [realtor.id for realtor in realtor_list]
        for i, offer in enumerate(data):
            self.get_tables(offer)
            validated_data, unknown_fields_list = self.make_dict_with_fields_info(listing_fields)
            unknown_fields |= unknown_fields_list
            if Listing.objects.filter(complex_id=int(offer['complex-id'])).exists():
                listing = Listing.objects.filter(complex_id=int(offer['complex-id'])).first()
                offer_updated_at = listing.updated_at
                if offer_updated_at != offer['updated_at']:
                    # update listing
                    validated_data['special_price'] = False
                    validated_data['is_fully_loaded'] = False
                    # print(validated_data)
                    # listing.update(**validated_data)
                    for attr, value in validated_data.items():
                        setattr(listing, attr, value)
                    listing.save()
                    print(
                        f"Offer complex-id {offer['complex-id']} with id=[{listing.id}] exist with the different updated_at {offer_updated_at} != {offer['updated_at']}, updated")
                    updated_records += 1
                else:
                    # pass
                    print(
                        f"Offer complex-id {offer['complex-id']} with id=[{listing.id}] exist with the same updated_at {offer['updated_at']}")
            else:
                # new listing
                validated_data['is_fully_loaded'] = False
                validated_data['source'] = 'alnair'
                validated_data['offer_type'] = 'sell'
                validated_data['special_price'] = False
                validated_data['realtor_id'] = choice(realtors_ids)
                validated_data['developer_id'] = developer_get_or_add(validated_data['developer_a_title_a_en'],
                                                                      validated_data['developer_a_title_a_ru'],
                                                                      validated_data['developer_a_title_a_ar'],
                                                                      validated_data['developer_a_logo'],
                                                                      Realtor,
                                                                      Developer).id
                new_listing = Listing.objects.create(**validated_data)

                print(f"New offer complex-id {offer['complex-id']} with id=[{new_listing.id}] inserted")
                added_records += 1

        return all_records, added_records, updated_records, unknown_fields

    def run(self):
        say_my_name()
        self.request_xml_db_file()
        all_records, added_records, updated_records, unknown_fields = self.load_data_into_db()
        result = self.info(all_records, added_records, updated_records, unknown_fields)
        print(result)

    def info(self, all_records, added_records, updated_records, unknown_fields):
        say_my_name()
        return (f"Loaded {all_records} records, added {added_records}, updated {updated_records}\n"
                f"finded {len(unknown_fields)} unknown fields [{unknown_fields}]")



def main():
    say_my_name()
    loader = DatabaseDownloader()
    loader.run()


if __name__ == "__main__":
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    main()
