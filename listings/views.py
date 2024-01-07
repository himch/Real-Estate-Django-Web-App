import json

from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_item = get_object_or_404(Listing, pk=listing_id)

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

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
    amenities = dict()
    for lang in ('ru', 'en', 'ar'):
        amenities[lang] = [amenity[lang] for amenity in json.loads(listing_item.listing_amenities) if lang in amenity]

    br_prices = json.loads(listing_item.listing_br_prices)
    if br_prices:
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
        min_area_m2 = min_area_ft2 = None
        min_price_rub = min_price_usd = min_price_eur = None
        min_price_m2_rub = min_price_m2_usd = min_price_m2_eur = None
        min_price_ft2_rub = min_price_ft2_usd = min_price_ft2_eur = None

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
        'listings': paged_listings
    }

    # return render(request, 'listings/listing.html', context)
    return render(request, 'includes/content/jk.html', context)


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
               'AEDEUR': 0.25
               }
    return round(value * courses[currency1 + currency2])
