import itertools

from django.core.paginator import Paginator
from django.db.models import Min, Max
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django_admin_geomap import geomap_context
from django.contrib import auth
from blog.models import Article
from catalogs.models import Catalog

from listings.models import Listing, District, Amenity, Price, Favorite
from listings.utils import convert
from pages.filters import buy_listing_filter
from pages.utils import check_number_var, check_str_var, is_htmx
from realtors.models import Realtor
from our_company.models import OurCompany


User = get_user_model()


def index(request):
    # print('request.LANGUAGE_CODE:', request.LANGUAGE_CODE)
    page = request.GET.get('page')

    our_company = OurCompany.objects.all().first()

    listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='sell')
    paginator = Paginator(listings, 6)
    paged_listings = paginator.get_page(page)

    rent_listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='rent')
    rent_paginator = Paginator(rent_listings, 6)
    paged_rent_listings = rent_paginator.get_page(page)

    catalogs = Catalog.objects.all()

    blog_articles = Article.objects.all()
    blog_paginator = Paginator(blog_articles, 6)
    paged_blog_articles = blog_paginator.get_page(1)

    context = {
        'our_company': our_company,
        'catalogs': catalogs,
        'blog_articles': paged_blog_articles,
        'rent_listings': paged_rent_listings,
        'listings': paged_listings
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/index.html', context)


def buy(request):
    # переменные для отображения состояния фильтров
    vars_filter = dict()

    # все обьекты недвижимости для продажи
    all_listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')

    # информация о собственной компании
    our_company = OurCompany.objects.all().first()

    # каталоги
    catalogs = Catalog.objects.all()

    # блог
    blog_articles = Article.objects.all()
    blog_paginator = Paginator(blog_articles, 6)
    paged_blog_articles = blog_paginator.get_page(1)

    # типы валют
    currencies = [{'value': 'usd', 'title': '$'},
                  {'value': 'eur', 'title': '€'},
                  {'value': 'rub', 'title': '₽'}, ]

    # типы единиц измерения площади
    areas = [{'value': 'sq_m', 'title': 'sq. m'},
             {'value': 'sq_ft', 'title': 'sq. ft'}]

    # множество типов недвижимости (например, residential_complex или village)
    estate_types = sorted(set(all_listings.values_list('type', flat=True).distinct()))

    # множество районов города
    districts = sorted(set(District.objects.filter(listing__in=all_listings).values_list('name', flat=True).distinct()))

    # множество удобств на обьекте недвижимости
    am = Amenity.objects.filter(listing__in=all_listings).values_list('en', 'ar', 'ru').distinct()
    amenities = [{'en': en, 'ar': ar, 'ru': ru, } for en, ar, ru in sorted(am)]

    listings_price = dict()
    listings_price['min'] = dict()
    listings_price['max'] = dict()
    present_currency = None
    # минимальная цена обьекта недвижимости из базы данных (AED to USD)
    for currency in ['AED', 'RUB', 'USD', 'EUR']:
        listings_price['min'][currency] = all_listings.filter(price_a_currency=currency).aggregate(Min('price_a_min'))['price_a_min__min']
        listings_price['max'][currency] = all_listings.filter(price_a_currency=currency).aggregate(Max('price_a_min'))['price_a_min__max']
        if listings_price['min'][currency]:
            present_currency = currency

    if present_currency:
        for currency in ['AED', 'RUB', 'USD', 'EUR']:
            listings_price['min'][currency] = convert(listings_price['min'][present_currency], present_currency, currency)
            listings_price['max'][currency] = convert(listings_price['max'][present_currency], present_currency, currency)

    print('prices', listings_price)

    # минимальная площадь обьекта недвижимости из базы данных
    listings_area_min_sq_m = Price.objects.aggregate(Min('min_area_m2'))['min_area_m2__min']
    listings_area_min_sq_ft = Price.objects.aggregate(Min('min_area_ft2'))['min_area_ft2__min']

    # максимальная площадь обьекта недвижимости из базы данных
    listings_area_max_sq_m = Price.objects.aggregate(Max('max_area_m2'))['max_area_m2__max']
    listings_area_max_sq_ft = Price.objects.aggregate(Max('max_area_ft2'))['max_area_ft2__max']

    # максимальное количество комнат обьекта недвижимости из базы данных
    func = lambda x: int(x[-1]) if x[-1].isdigit() else 0
    rooms = list(map(func, Price.objects.exclude(key__isnull=True).filter(listing__in=all_listings).values_list('key', flat=True).distinct()))
    if rooms:
        listings_max_rooms = max(rooms)
    else:
        listings_max_rooms = 0

    # отфильтрованные обьекты в соотвествии с заданными на странице фильтрами
    listings = buy_listing_filter(request.GET,
                                  queryset=all_listings,
                                  language_code=request.LANGUAGE_CODE,
                                  estate_types=estate_types,
                                  districts=districts,
                                  amenities=amenities)

    # точки на карте для всех отфильтрованных обьектов недвижимости для продажи
    geo_context = geomap_context(listings, auto_zoom="20")

    # разбиение обьектов на порции-страницы для отображения в виде списка
    page = request.GET.get('page')
    paginator = Paginator(listings, 6)
    paged_listings = paginator.get_page(page)

    # обьекты недвижимости для аренды для ленты
    rent_page = request.GET.get('page')
    rent_listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='rent')
    rent_paginator = Paginator(rent_listings, 6)
    paged_rent_listings = rent_paginator.get_page(rent_page)

    # переменные для отображения состояния фильтров в начале страницы
    variables = {var: check_number_var(request.GET, var) for var in ['price_min', 'price_max']}
    vars_filter.update(variables)

    estate_types_choices = {'estate_type_' + estate_type:
                                {'value': request.GET.get('estate_type_' + estate_type),
                                 'title': estate_type}
                            for estate_type in estate_types}
    if not any(value['value'] for value in estate_types_choices.values()):
        estate_types_choices = {'estate_type_' + estate_type:
                                    {'value': estate_type,
                                     'title': estate_type}
                                for estate_type in estate_types}

    # переменные для отображения состояния фильтров в buy_big_modal_filter.html

    variables = {var: check_number_var(request.GET, var) for var in ['price_rub_min', 'price_rub_max', 'price_dollar_min', 'price_dollar_max', 'price_euro_min', 'price_euro_max']}
    vars_filter.update(variables)

    vars_filter['currency'] = check_str_var(request.GET, 'currency', currencies[0]['value'])
    vars_filter['area'] = check_str_var(request.GET, 'area', areas[0]['value'])
    vars_filter['area_min'] = check_str_var(request.GET, 'area_min', listings_area_min_sq_m)
    vars_filter['area_max'] = check_str_var(request.GET, 'area_max', listings_area_max_sq_m)
    vars_filter['fut_min'] = check_str_var(request.GET, 'fut_min', listings_area_min_sq_ft)
    vars_filter['fut_max'] = check_str_var(request.GET, 'fut_max', listings_area_max_sq_m)
    variables = {'listings_price_min_aed': listings_price['min']['AED'],
                 'listings_price_min_usd': listings_price['min']['USD'],
                 'listings_price_min_eur': listings_price['min']['EUR'],
                 'listings_price_min_rub': listings_price['min']['RUB'],
                 'listings_price_max_aed': listings_price['max']['AED'],
                 'listings_price_max_usd': listings_price['max']['USD'],
                 'listings_price_max_eur': listings_price['max']['EUR'],
                 'listings_price_max_rub': listings_price['max']['RUB'],
                 'listings_area_min_sq_m': listings_area_min_sq_m,
                 'listings_area_min_sq_ft': listings_area_min_sq_ft,
                 'listings_area_max_sq_m': listings_area_max_sq_m,
                 'listings_area_max_sq_ft': listings_area_max_sq_ft,
                 'listings_max_rooms': listings_max_rooms}
    vars_filter.update(variables)

    print(request.GET.get('currency'))
    print(request.GET.get('area'))
    print(request.GET.get('price_rub_min'))
    print(request.GET.get('price_rub_max'))
    print(request.GET.get('price_dollar_min'))
    print(request.GET.get('price_dollar_max'))
    print(request.GET.get('price_euro_min'))
    print(request.GET.get('price_euro_max'))
    print(request.GET.get('area_min'))
    print(request.GET.get('area_max'))
    print(request.GET.get('fut_min'))
    print(request.GET.get('fut_max'))

    districts_choices = {'district_' + district:
                             {'value': request.GET.get('district_' + district),
                              'title': district}
                         for district in districts}
    if not any(value['value'] for value in districts_choices.values()):
        districts_choices = {'district_' + district:
                                 {'value': district,
                                  'title': district}
                             for district in districts}

    amenities_choices = {'amenity_' + amenity['en']:
                             {'value': request.GET.get('amenity_' + amenity['en']),
                              'title': amenity[request.LANGUAGE_CODE]}
                         for amenity in amenities}
    if not any(value['value'] for value in amenities_choices.values()):
        amenities_choices = {'amenity_' + amenity['en']:
                                 {'value': amenity['en'],
                                  'title': amenity[request.LANGUAGE_CODE]}
                             for amenity in amenities}

    print(vars_filter)

    context = {
        'our_company': our_company,
        'catalogs': catalogs,
        'blog_articles': paged_blog_articles,
        'len_listings': len(listings),
        'rent_listings': paged_rent_listings,
        'listings': paged_listings,
        'currencies': currencies,
        'areas': areas,
        'estate_types_choices': estate_types_choices,
        'districts_choices': districts_choices,
        'amenities_choices': amenities_choices,
        'vars_filter': vars_filter,
    }

    context.update(geo_context)
    if is_htmx(request):
        return render(request,
                      "includes/buy/buy_loaded_block.html",
                      {"listings": paged_listings,
                       'len_listings': len(listings)
                       }
                      )
    return render(request, 'includes/content/buy.html', context)


def arenda(request):
    # переменные для отображения состояния фильтров
    vars_filter = dict()

    # все обьекты недвижимости для аренды
    all_listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='rent')

    # информация о собственной компании
    our_company = OurCompany.objects.all().first()

    # каталоги
    catalogs = Catalog.objects.all()

    # блог
    blog_articles = Article.objects.all()
    blog_paginator = Paginator(blog_articles, 6)
    paged_blog_articles = blog_paginator.get_page(1)

    # типы валют
    currencies = [{'value': 'usd', 'title': '$'},
                  {'value': 'eur', 'title': '€'},
                  {'value': 'rub', 'title': '₽'}, ]

    # типы единиц измерения площади
    areas = [{'value': 'sq_m', 'title': 'sq. m'},
             {'value': 'sq_ft', 'title': 'sq. ft'}]

    # множество типов недвижимости (например, residential_complex или village)
    estate_types = sorted(set(all_listings.values_list('type', flat=True).distinct()))

    # множество районов города
    districts = sorted(set(District.objects.filter(listing__in=all_listings).values_list('name', flat=True).distinct()))

    # множество удобств на обьекте недвижимости
    am = Amenity.objects.filter(listing__in=all_listings).values_list('en', 'ar', 'ru').distinct()
    amenities = [{'en': en, 'ar': ar, 'ru': ru, } for en, ar, ru in sorted(am)]

    listings_price = dict()
    listings_price['min'] = dict()
    listings_price['max'] = dict()
    present_currency = None
    # минимальная цена обьекта недвижимости из базы данных (AED to USD)
    for currency in ['AED', 'RUB', 'USD', 'EUR']:
        listings_price['min'][currency] = all_listings.filter(price_a_currency=currency).aggregate(Min('price_a_min'))['price_a_min__min']
        listings_price['max'][currency] = all_listings.filter(price_a_currency=currency).aggregate(Max('price_a_min'))['price_a_min__max']
        if listings_price['min'][currency]:
            present_currency = currency

    if present_currency:
        for currency in ['AED', 'RUB', 'USD', 'EUR']:
            listings_price['min'][currency] = convert(listings_price['min'][present_currency], present_currency, currency)
            listings_price['max'][currency] = convert(listings_price['max'][present_currency], present_currency, currency)

    print('prices', listings_price)

    # минимальная площадь обьекта недвижимости из базы данных
    listings_area_min_sq_m = Price.objects.aggregate(Min('min_area_m2'))['min_area_m2__min']
    listings_area_min_sq_ft = Price.objects.aggregate(Min('min_area_ft2'))['min_area_ft2__min']

    # максимальная площадь обьекта недвижимости из базы данных
    listings_area_max_sq_m = Price.objects.aggregate(Max('max_area_m2'))['max_area_m2__max']
    listings_area_max_sq_ft = Price.objects.aggregate(Max('max_area_ft2'))['max_area_ft2__max']

    # максимальное количество комнат обьекта недвижимости из базы данных
    func = lambda x: int(x[-1]) if x[-1].isdigit() else 0
    rooms = list(map(func, Price.objects.exclude(key__isnull=True).filter(listing__in=all_listings).values_list('key', flat=True).distinct()))
    if rooms:
        listings_max_rooms = max(rooms)
    else:
        listings_max_rooms = 0

    # отфильтрованные обьекты в соотвествии с заданными на странице фильтрами
    listings = buy_listing_filter(request.GET,
                                  queryset=all_listings,
                                  language_code=request.LANGUAGE_CODE,
                                  estate_types=estate_types,
                                  districts=districts,
                                  amenities=amenities)

    # точки на карте для всех отфильтрованных обьектов недвижимости для продажи
    geo_context = geomap_context(listings, auto_zoom="20")

    # разбиение обьектов на порции-страницы для отображения в виде списка
    page = request.GET.get('page')
    print('page', page)
    paginator = Paginator(listings, 6)
    paged_listings = paginator.get_page(page)

    # переменные для отображения состояния фильтров в начале страницы
    variables = {var: check_number_var(request.GET, var) for var in ['price_min', 'price_max']}
    vars_filter.update(variables)

    estate_types_choices = {'estate_type_' + estate_type:
                                {'value': request.GET.get('estate_type_' + estate_type),
                                 'title': estate_type}
                            for estate_type in estate_types}
    if not any(value['value'] for value in estate_types_choices.values()):
        estate_types_choices = {'estate_type_' + estate_type:
                                    {'value': estate_type,
                                     'title': estate_type}
                                for estate_type in estate_types}

    # переменные для отображения состояния фильтров в rent_big_modal_filter.html

    variables = {var: check_number_var(request.GET, var) for var in ['Bedroom_studio', 'Bedroom_1', 'Bedroom_2', 'Bedroom_3', 'Bedroom_4plus']}
    vars_filter.update(variables)

    variables = {var: check_number_var(request.GET, var) for var in ['price_rub_min', 'price_rub_max', 'price_dollar_min', 'price_dollar_max', 'price_euro_min', 'price_euro_max']}
    vars_filter.update(variables)

    vars_filter['currency'] = check_str_var(request.GET, 'currency', currencies[0]['value'])
    vars_filter['area'] = check_str_var(request.GET, 'area', areas[0]['value'])
    vars_filter['area_min'] = check_str_var(request.GET, 'area_min', listings_area_min_sq_m)
    vars_filter['area_max'] = check_str_var(request.GET, 'area_max', listings_area_max_sq_m)
    vars_filter['fut_min'] = check_str_var(request.GET, 'fut_min', listings_area_min_sq_ft)
    vars_filter['fut_max'] = check_str_var(request.GET, 'fut_max', listings_area_max_sq_m)
    variables = {'listings_price_min_aed': listings_price['min']['AED'],
                 'listings_price_min_usd': listings_price['min']['USD'],
                 'listings_price_min_eur': listings_price['min']['EUR'],
                 'listings_price_min_rub': listings_price['min']['RUB'],
                 'listings_price_max_aed': listings_price['max']['AED'],
                 'listings_price_max_usd': listings_price['max']['USD'],
                 'listings_price_max_eur': listings_price['max']['EUR'],
                 'listings_price_max_rub': listings_price['max']['RUB'],
                 'listings_area_min_sq_m': listings_area_min_sq_m,
                 'listings_area_min_sq_ft': listings_area_min_sq_ft,
                 'listings_area_max_sq_m': listings_area_max_sq_m,
                 'listings_area_max_sq_ft': listings_area_max_sq_ft,
                 'listings_max_rooms': listings_max_rooms}
    vars_filter.update(variables)

    print(request.GET.get('currency'))
    print(request.GET.get('area'))
    print(request.GET.get('price_rub_min'))
    print(request.GET.get('price_rub_max'))
    print(request.GET.get('price_dollar_min'))
    print(request.GET.get('price_dollar_max'))
    print(request.GET.get('price_euro_min'))
    print(request.GET.get('price_euro_max'))
    print(request.GET.get('area_min'))
    print(request.GET.get('area_max'))
    print(request.GET.get('fut_min'))
    print(request.GET.get('fut_max'))

    districts_choices = {'district_' + district:
                             {'value': request.GET.get('district_' + district),
                              'title': district}
                         for district in districts}
    if not any(value['value'] for value in districts_choices.values()):
        districts_choices = {'district_' + district:
                                 {'value': district,
                                  'title': district}
                             for district in districts}

    amenities_choices = {'amenity_' + amenity['en']:
                             {'value': request.GET.get('amenity_' + amenity['en']),
                              'title': amenity[request.LANGUAGE_CODE]}
                         for amenity in amenities}
    if not any(value['value'] for value in amenities_choices.values()):
        amenities_choices = {'amenity_' + amenity['en']:
                                 {'value': amenity['en'],
                                  'title': amenity[request.LANGUAGE_CODE]}
                             for amenity in amenities}

    print(vars_filter)

    context = {
        'our_company': our_company,
        'blog_articles': paged_blog_articles,
        'len_listings': len(listings),
        'listings': paged_listings,
        'currencies': currencies,
        'areas': areas,
        'estate_types_choices': estate_types_choices,
        'districts_choices': districts_choices,
        'amenities_choices': amenities_choices,
        'vars_filter': vars_filter,
    }

    context.update(geo_context)

    if is_htmx(request):
        return render(request,
                      "includes/rent/rent_loaded_block.html",
                      {"listings": paged_listings,
                       'len_listings': len(listings)
                       }
                      )
    return render(request, 'includes/content/arenda.html', context)


def izbrannoe(request):
    user = auth.get_user(request)

    favorites = user.profile.favorites.all()

    listings = favorites.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')
    rent_listings = favorites.order_by('-list_date').filter(is_fully_loaded=True, offer_type='rent')

    our_company = OurCompany.objects.all().first()

    blog_articles = Article.objects.all()
    blog_paginator = Paginator(blog_articles, 6)
    paged_blog_articles = blog_paginator.get_page(1)

    context = {
        'our_company': our_company,
        'listings': listings,
        'rent_listings': rent_listings,
        'blog_articles': paged_blog_articles,
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/izbrannoe.html', context)


def sravnenie(request):
    user = auth.get_user(request)

    bookmarks = user.profile.bookmarks.all()
    listings = bookmarks.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')

    our_company = OurCompany.objects.all().first()
    catalogs = Catalog.objects.all()

    blog_articles = Article.objects.all()
    blog_paginator = Paginator(blog_articles, 6)
    paged_blog_articles = blog_paginator.get_page(1)

    context = {
        'our_company': our_company,
        'catalogs': catalogs,
        'listings': listings,
        'blog_articles': paged_blog_articles,
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/sravnenie.html', context)


def about(request):
    our_company = OurCompany.objects.all().first()

    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'our_company': our_company,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/dadi.html', context)


def katalogi(request):
    our_company = OurCompany.objects.all().first()
    catalogs = Catalog.objects.all()

    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'our_company': our_company,
        'catalogs': catalogs,
        'blog_range': range(3),
        'listings': paged_listings,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/katalogi.html', context)


# def arenda_single(request):
#     # Get all realtors
#     realtors = Realtor.objects.order_by('-hire_date')
#
#     # Get MVP
#     mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
#
#     listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True)
#
#     paginator = Paginator(listings, 6)
#     page = request.GET.get('page')
#     paged_listings = paginator.get_page(page)
#
#     context = {
#         'listings': paged_listings,
#         'realtors': realtors,
#         'mvp_realtors': mvp_realtors
#     }
#
#     return render(request, 'includes/content/arenda-single.html', context)
