from random import choice

from developers.models import Developer
from listings.models import Listing
from realtors.models import Realtor


def scan_developers():
    listings = Listing.objects.all()
    realtor_list = Realtor.objects.all()
    realtors_ids = [realtor.id for realtor in realtor_list]
    unknown_developer, created = Developer.objects.get_or_create(slug='unknown',
                                                                 defaults={'title_en': 'The Unknown',
                                                                           'title_ru': 'The Unknown',
                                                                           'title_ar': 'The Unknown',
                                                                           'logo': '/img/unknown.jpeg',
                                                                           'realtor_id': choice(realtors_ids)})
    count = 0
    for listing in listings:
        titles = [listing.developer_a_title_a_en, listing.developer_a_title_a_ru, listing.developer_a_title_a_ar]
        titles = list(filter(None, titles))
        if titles:
            title_en = listing.developer_a_title_a_en if listing.developer_a_title_a_en else titles[0]
            title_ru = listing.developer_a_title_a_ru if listing.developer_a_title_a_en else titles[0]
            title_ar = listing.developer_a_title_a_ar if listing.developer_a_title_a_en else titles[0]
            developer, created = Developer.objects.get_or_create(title_en=title_en,
                                                                 defaults={'title_en': title_en,
                                                                           'title_ru': title_ru,
                                                                           'title_ar': title_ar,
                                                                           'logo': listing.developer_a_logo,
                                                                           'realtor_id': choice(realtors_ids)})
        else:
            developer = unknown_developer
        listing.developer = developer
        listing.save()

    return count
