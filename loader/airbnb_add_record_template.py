import os
from random import choice

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')

import django
django.setup()

from listings.models import Listing
from realtors.models import Realtor


realtor_list = Realtor.objects.all()
realtors_ids = [realtor.id for realtor in realtor_list]

listing = Listing()
listing.source = 'airbnb'
listing.offer_type = 'rent'
listing.url = {url}

listing.realtor_id = choice(realtors_ids)
listing.complex_id = {complex_id}
listing.type = """rooms"""
listing.photo = {photo}
listing.title_a_ru = {title_a_ru}
listing.title_a_en = {title_a_en}
listing.title_a_ar = {title_a_ar}
listing.description_a_ru = {description_a_ru}
listing.description_a_en = {description_a_en}
listing.description_a_ar = {description_a_ar}
listing.price_on_request = 0
listing.listing_amenities = {listing_amenities}
listing.listing_districts = {listing_districts}
listing.address = {address}
listing.listing_album = {listing_album}
listing.price_a_min = {price_a_min}
listing.price_a_max = {price_a_max}
listing.price_a_currency = {price_a_currency}
listing.updated_at = {updated_at}
listing.is_sold_out = 0
listing.save()
