import os

import xmltodict as xmltodict
# from django.db import models
# import untangle
import sqlite3
import json
import asyncio


# from listings.models import Listing
from loader import Loader
from realestate.settings import DATABASES
from utils import is_int, is_float


class Downloader(Loader):
    FILE_URL = 'https://api.alnair.ae/v1/feed/download/333035345fa2fab400233833bd5f31/rc'
    database_dict = None

    def __init__(self, url=FILE_URL):
        super().__init__(url)

    async def request_xml_db_file(self):
        content = await self.request_content()
        self.database_dict = xmltodict.parse(content, xml_attribs=True)


class SQLExecutor:
    DATABASE_NAME = DATABASES['default']['NAME']
    connection = None
    cursor = None

    def __init__(self, database_name=DATABASE_NAME):
        self.connection = sqlite3.connect(database_name)
        if self.connection is not None:
            self.cursor = self.connection.cursor()

    async def execute_sql(self, sql, parameters=(), commit=True):
        if not self.cursor:
            self.cursor = self.connection.cursor()
        if parameters:
            q = self.cursor.execute(sql, parameters)
        else:
            q = self.cursor.execute(sql)
        if commit:
            self.connection.commit()
        return q

    async def close_connection(self):
        if self.connection:
            self.connection.close()

    async def check_table_exist(self, table):
        check_sqlite_table_exist_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';"
        q = await self.execute_sql(check_sqlite_table_exist_query, commit=False)
        data = q.fetchone()
        table_exist = data and (data[0] == table)
        return table_exist

    async def check_column_exist(self, table, column):
        check_sqlite_col_exist_query = f"SELECT name FROM pragma_table_info('{table}') WHERE name='{column}';"
        q = await self.execute_sql(check_sqlite_col_exist_query, commit=False)
        data = q.fetchone()
        column_exist = data and (data[0] == column)
        return column_exist

    async def add_column(self, table, column, column_type):
        alter_sqlite_col_query = f"ALTER TABLE {table} ADD COLUMN {column} {column_type};"
        await self.execute_sql(alter_sqlite_col_query)


class DatabaseDownloader(Downloader, SQLExecutor):
    TOP_TABLE_PREFIX = 'listings_'
    TOP_TABLE_NAME = 'listing'
    sql_for_create_table = dict()
    sql_for_insert_records = dict()
    python_for_insert_records = dict()
    python_for_create_table = dict()
    tables = dict()

    def __init__(self, *args):
        Downloader.__init__(self, *args)
        SQLExecutor.__init__(self, *args)

    async def get_fields(self, table_name, key, item, table_func):
        # возвращает список полей таблицы
        key = key.replace('-', '_')
        if isinstance(item, dict):
            result = []
            for k in item:
                if k != 'id':
                    if len(item) > 1:
                        result += await self.get_fields(table_name,
                                                        ((key + '_a_') if key else '') + k,
                                                        item[k],
                                                        table_func)
                    else:
                        result += await self.get_fields(table_name, key, item[k], table_func)
            return result
        elif isinstance(item, list):
            # if table_func:
            #     await table_func(item[0], table_name=table_name + '_' + key, fk=(f'{table_name}_id', 'INT', None), )
            return (table_name + '_' + key, 'LIST', json.dumps(item)),
        elif is_int(item):
            return (key if key else "value", 'INT', item),
        elif is_float(item):
            return (key if key else "value", 'REAL', item),
        else:
            return (key if key else "value", 'CHAR', item),

    async def get_tables(self, item, table_name=TOP_TABLE_NAME, fk=None):
        if item:
            fields = []
            if fk:
                fields.append(fk)
            fields += await self.get_fields(table_name, '', item, self.get_tables)
            if fields:
                self.tables[table_name] = fields

    async def make_sql_for_create_tables(self):
        types = {'INT': 'INT',
                 'REAL': 'REAL',
                 'CHAR': 'CHAR',
                 'LIST': 'CHAR'}
        for table in self.tables:
            sql = f'''
            CREATE TABLE IF NOT EXISTS {table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                {', '.join(f'{field} {types[field_type]}' for field, field_type, item in self.tables[table])}
                );
            '''
            self.sql_for_create_table[table] = sql
            print(sql)

    async def make_sql_for_insert_record(self):
        for table in self.tables:
            sql = f'''
            INSERT INTO {table} (
                {', '.join(field for field, field_type, item in self.tables[table])}
                ) VALUES ({', '.join('?' for field, field_type, item in self.tables[table])});
            '''
            self.sql_for_insert_records[table] = sql
            print(sql)

    async def make_python_for_insert_record(self):
        for table in self.tables:
            template = ''
            i = 0
            for field, field_type, item in self.tables[table]:
                template += f'listing.{field} = {{{field}}}\n'
                i += 1
            template += 'listing.save()'
            self.python_for_insert_records[table] = template
            # print(template)

    async def make_python_for_create_tables(self):
        types = {'INT': 'IntegerField(null=True)',
                 'REAL': 'FloatField(null=True)',
                 'CHAR': 'TextField(blank=True, null=True)',
                 'LIST': 'JSONField(blank=True, null=True)'}
        with open("python_create_tables.py", "w", encoding='utf-8') as file:
            for table in self.tables:
                new_line = '\n    '
                code = (f"class {table.capitalize()}(models.Model):{new_line}" +
                        new_line.join(f'{field} = models.{types[field_type]}'
                                      for field, field_type, item in self.tables[table])) + '\n\n'
                self.python_for_create_table[table] = code
                print(code)
                file.write(code)

    async def create_tables(self):
        types = {'INT': 'INT',
                 'REAL': 'REAL',
                 'CHAR': 'CHAR',
                 'LIST': 'CHAR'}
        await self.get_tables(self.database_dict['realty-feed']['offers'][0])
        for table in self.sql_for_create_table:
            if await self.check_table_exist(table):
                print('table', table, 'exist')
                for field, field_type, item in self.tables[table]:
                    if not await self.check_column_exist(table, field):
                        print('table', table, 'column', field, 'NOT exist')
                        await self.add_column(table, field, types[field_type])
                    else:
                        print('table', table, 'column', field, 'exist')
            else:
                print('table', table, 'NOT exist')
                await self.execute_sql(self.sql_for_create_table[table])

    async def offer_exist(self, complex_id):
        sql = f'SELECT * FROM {self.TOP_TABLE_PREFIX + self.TOP_TABLE_NAME} WHERE complex_id={complex_id};'
        q = await self.execute_sql(sql, commit=False)
        data = q.fetchone()
        return data is not None

    async def insert_record_sql(self, record, table_name=TOP_TABLE_NAME):
        if record:
            fields = []
            # if fk:
            #     fields.append(fk)
            fields += await self.get_fields(table_name, '', record, None)
            if fields:
                parameters = [item for field, field_type, item in self.tables[table_name]]
                await self.execute_sql(self.sql_for_insert_records[table_name], parameters)

    async def insert_record_python(self, record, table_name=TOP_TABLE_NAME):
        if record:
            # print('len record =', len(record))
            fields = []
            # if fk:
            #     fields.append(fk)
            # fields += await self.get_fields(table_name, '', record, None)
            # print('len fields =', len(fields))
            if True:  # fields
                k = '"' * 3
                parameters = []
                for field, field_type, item in self.tables[table_name]:
                    if field_type == 'INT':
                        parameters.append(f'{field}={int(item)}')
                    elif field_type == 'REAL':
                        parameters.append(f'{field}={float(item)}')
                    elif field_type == 'CHAR':
                        if item is None:
                            parameters.append(f'{field}=None')
                        else:
                            parameters.append(f"{field}='''{k + item + k}'''")
                    elif field_type == 'LIST':
                        if item is None:
                            parameters.append(f'{field}=None')
                        else:
                            parameters.append(f"{field}='''{k + item + k}'''")
                # print('len parameters =', len(parameters))
                templ = ("import os\n"
                         "from random import choice\n"
                         "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')\n"
                         "import django\n"
                         "django.setup()\n"
                         "from listings.models import Listing\n"
                         "from realtors.models import Realtor\n"                       
                         "realtor_list = Realtor.objects.all()\n"
                         "realtors_ids = [realtor.id for realtor in realtor_list]\n"
                         "listing = Listing()\n"
                         "listing.realtor_id = choice(realtors_ids)\n")
                code = self.python_for_insert_records[table_name]
                command = 'code.format(' + ', '.join(parameters) + ')'
                # print(command)

                code_for_exec = templ + eval(command, globals(), locals())
                # print(code_for_exec)
                with open("python_add_record.py", "w", encoding='utf-8') as file:
                    file.write(code_for_exec.encode('utf-8', 'replace').decode())
                os.system('python python_add_record.py')
                # exec(code_for_exec, globals(), locals())

    async def delete_record(self, complex_id):
        sql = f'DELETE FROM {self.TOP_TABLE_PREFIX + self.TOP_TABLE_NAME} WHERE complex_id={complex_id};'
        q = await self.execute_sql(sql)

    async def load_data_into_db(self):
        for offer in self.database_dict['realty-feed']['offers'][:25]:
            print('work with offer complex-id', offer['complex-id'])
            if await self.offer_exist(offer['complex-id']):
                await self.delete_record(offer['complex-id'])
            # await self.insert_record_sql(offer)
            await self.get_tables(offer)
            await self.make_python_for_insert_record()
            await self.insert_record_python(offer)
            # break

    async def run(self):
        await self.request_xml_db_file()
        # await self.get_tables(self.database_dict['realty-feed']['offers'][0])
        # await self.make_sql_for_create_tables()
        # await self.create_tables()
        # await self.make_sql_for_insert_record()
        # await self.make_python_for_insert_record()
        # await self.make_python_for_create_tables()
        await self.load_data_into_db()
        await self.close_connection()

    async def info(self):
        return f"Loaded {len(self.database_dict['realty-feed']['offers'])} records"


async def main():
    loader = DatabaseDownloader()
    await loader.run()
    print(await loader.info())


if __name__ == "__main__":
    asyncio.run(main())
