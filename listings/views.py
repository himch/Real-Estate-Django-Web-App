import json
import ast

from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.translation import ugettext as _

from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing


# def index(request):
#     listings = Listing.objects.order_by('-list_date').filter(is_published=True)
#
#     paginator = Paginator(listings, 6)
#     page = request.GET.get('page')
#     paged_listings = paginator.get_page(page)
#
#     context = {
#         'listings': paged_listings
#     }
#
#     return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_item = get_object_or_404(Listing, pk=listing_id)

    realtor = listing_item.realtor

    listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='sell')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    if listing_item.listing_br_prices:
        br_prices = json.loads(listing_item.listing_br_prices)
        print(type(br_prices), br_prices)
        br_price = br_prices[0]
        currency = br_price['currency']
        min_price = float(br_price['min_price'])
        min_price_rub = convert(min_price, currency, 'RUB')
        min_price_usd = convert(min_price, currency, 'USD')
        min_price_eur = convert(min_price, currency, 'EUR')
        min_price_m2 = float(br_price['min_price_m2'])
        min_price_m2_rub = convert(min_price_m2, currency, 'RUB')
        min_price_m2_usd = convert(min_price_m2, currency, 'USD')
        min_price_m2_eur = convert(min_price_m2, currency, 'EUR')
        min_price_ft2_rub = round(min_price_m2_rub / 10.7639)
        min_price_ft2_usd = round(min_price_m2_usd / 10.7639)
        min_price_ft2_eur = round(min_price_m2_eur / 10.7639)
        min_area_m2 = round(float(br_price['min_area']['m2']))
    else:
        br_prices = None
        min_area_m2 = min_area_ft2 = None
        min_price_rub = min_price_usd = min_price_eur = None
        min_price_m2_rub = min_price_m2_usd = min_price_m2_eur = None
        min_price_ft2_rub = min_price_ft2_usd = min_price_ft2_eur = None

    amenities = dict()
    for lang in ('ru', 'en', 'ar'):
        amenities[lang] = [amenity[lang] for amenity in json.loads(listing_item.listing_amenities) if lang in amenity]

    context = {
        'br_prices': br_prices,
        'min_area_m2': min_area_m2,

        'min_price_rub': min_price_rub,
        'min_price_usd': min_price_usd,
        'min_price_eur': min_price_eur,

        'min_price_m2_rub': min_price_m2_rub,
        'min_price_m2_usd': min_price_m2_usd,
        'min_price_m2_eur': min_price_m2_eur,

        'min_price_ft2_rub': min_price_ft2_rub,
        'min_price_ft2_usd': min_price_ft2_usd,
        'min_price_ft2_eur': min_price_ft2_eur,

        'amenities_ru': amenities['ru'],
        'amenities_en': amenities['en'],
        'amenities_ar': amenities['ar'],
        'listing': listing_item,
        'listings': paged_listings,
        'realtor': realtor
    }

    # return render(request, 'listings/listing.html', context)
    return render(request, 'includes/content/jk.html', context)


def rent(request, listing_id):
    listing_item = get_object_or_404(Listing, pk=listing_id)

    realtor = listing_item.realtor

    listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='rent')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    if (listing_item.price_a_min and listing_item.price_a_currency) or listing_item.listing_br_prices:
        if listing_item.listing_br_prices:
            br_prices = json.loads(listing_item.listing_br_prices)
            br_price = br_prices[0]
            currency = br_price['currency']
            min_price = float(br_price['min_price'])
            min_price_m2 = float(br_price['min_price_m2'])
            min_area_m2 = round(float(br_price['min_area']['m2']))
        else:
            br_prices = None
            currency = listing_item.price_a_currency
            min_price = int(round(float(listing_item.price_a_min), -1))
            min_area_m2 = 50
            min_price_m2 = min_price / min_area_m2
        min_price_rub = convert(min_price, currency, 'RUB')
        min_price_usd = convert(min_price, currency, 'USD')
        min_price_eur = convert(min_price, currency, 'EUR')
        max_price_rub = int(round(min_price_rub * 1.33, -1))
        max_price_usd = int(round(min_price_usd * 1.33, -1))
        max_price_eur = int(round(min_price_eur * 1.33, -1))
        min_price_month_rub = int(round(min_price_rub * 30 / 2.7, -1))
        min_price_month_usd = int(round(min_price_usd * 30 / 2.7, -1))
        min_price_month_eur = int(round(min_price_eur * 30 / 2.7, -1))
        min_price_m2_rub = convert(min_price_m2, currency, 'RUB')
        min_price_m2_usd = convert(min_price_m2, currency, 'USD')
        min_price_m2_eur = convert(min_price_m2, currency, 'EUR')
        min_price_ft2_rub = int(round(min_price_m2_rub / 10.7639, -1))
        min_price_ft2_usd = int(round(min_price_m2_usd / 10.7639, -1))
        min_price_ft2_eur = int(round(min_price_m2_eur / 10.7639, -1))
    else:
        br_prices = None
        min_area_m2 = min_area_ft2 = None
        min_price_rub = min_price_usd = min_price_eur = None
        min_price_m2_rub = min_price_m2_usd = min_price_m2_eur = None
        min_price_ft2_rub = min_price_ft2_usd = min_price_ft2_eur = None
        min_price_month_rub = min_price_month_usd = min_price_month_eur = None
        max_price_rub = max_price_usd = max_price_eur = None

    amenities = dict()
    for lang in ('ru', 'en', 'ar'):
        amenities[lang] = [amenity[lang] for amenity in json.loads(listing_item.listing_amenities) if lang in amenity]

    context = {
        'br_prices': br_prices,
        'min_area_m2': min_area_m2,

        'min_price_rub': min_price_rub,
        'min_price_usd': min_price_usd,
        'min_price_eur': min_price_eur,

        'max_price_rub': max_price_rub,
        'max_price_usd': max_price_usd,
        'max_price_eur': max_price_eur,

        'min_price_month_rub': min_price_month_rub,
        'min_price_month_usd': min_price_month_usd,
        'min_price_month_eur': min_price_month_eur,

        'min_price_m2_rub': min_price_m2_rub,
        'min_price_m2_usd': min_price_m2_usd,
        'min_price_m2_eur': min_price_m2_eur,

        'min_price_ft2_rub': min_price_ft2_rub,
        'min_price_ft2_usd': min_price_ft2_usd,
        'min_price_ft2_eur': min_price_ft2_eur,

        'amenities_ru': amenities['ru'][:9],
        'amenities_en': amenities['en'][:9],
        'amenities_ar': amenities['ar'][:9],
        'listing': listing_item,
        'listings': paged_listings,
        'realtor': realtor
    }

    # return render(request, 'listings/listing.html', context)
    return render(request, 'includes/content/arenda-single.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)


def convert(value, currency1, currency2):
    courses = {'AEDRUB': 24.76,
               'AEDUSD': 0.27,
               'AEDEUR': 0.25,
               'AEDAED': 1,
               'RUBUSD': 0.011,
               'RUBEUR': 0.01,
               'RUBRUB': 1,
               }
    return int(round(value * courses[currency1 + currency2], -1))

# amenities_type = {('air', 'conditioner'): 'air-conditioner',
#                   ('balcony', ): 'balcony',
#                   ('balcony', ): 'bed',
#                   'celebrate',
#                   'clock',
#                   'clothes-hanger',
#                   'dishwasher',
#                   'dont-smoke',
#                   'door',
#                   'element',
#                   'farming',
#                   'guard',
#                   'key-chain',
#                   'location-pin',
#                   'monitor',
#                   'parking',
#                   'paw',
#                   'profile-2user',
#                   'shower',
#                   'slider',
#                   'swimming-pool',
#                   'tray',
#                   'wardrobe',
#                   'weight',
#                   'wifi'
#                   }
