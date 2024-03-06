import random
from itertools import chain

from django.core.paginator import Paginator
from django.db.models import Min, Max
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django_admin_geomap import geomap_context
from django.contrib import auth
from django.urls import resolve
from blog.models import Article
from catalogs.models import Catalog

from listings.models import Listing, District, Amenity, Price, Favorite, SUITABLE_FOR_CHOICES
from listings.utils import convert
from pages.filters import listing_filter
from pages.utils import check_number_var, check_str_var, is_htmx, create_choices, get_min_max_listings_prices
from realtors.models import Realtor
from our_company.models import OurCompany

OFFERS_IN_CAROUSEL = 6

User = get_user_model()


def get_random(objects, number):
    try:
        return random.sample(list(objects), number)
    except ValueError:
        return objects


def index(request):
    our_company = OurCompany.objects.all().first()

    listings = Listing.sell_objects.filter(special_price=True)
    if listings.count() < OFFERS_IN_CAROUSEL:
        random_listings = get_random(Listing.sell_objects.filter(special_price=False),
                                     OFFERS_IN_CAROUSEL - listings.count())
        listings = list(chain(listings, random_listings))
    random_listings = get_random(listings, OFFERS_IN_CAROUSEL)

    rent_listings = Listing.rent_objects.filter(special_price=True)
    if rent_listings.count() < OFFERS_IN_CAROUSEL:
        random_rent_listings = get_random(Listing.rent_objects.filter(special_price=False),
                                          OFFERS_IN_CAROUSEL - rent_listings.count())
        rent_listings = list(chain(rent_listings, random_rent_listings))
    random_rent_listings = get_random(rent_listings, OFFERS_IN_CAROUSEL)

    random_catalogs = get_random(Catalog.objects.all(), OFFERS_IN_CAROUSEL)

    random_blog_articles = get_random(Article.objects.all(), OFFERS_IN_CAROUSEL)

    context = {
        'our_company': our_company,
        'catalogs': random_catalogs,
        'blog_articles': random_blog_articles,
        'rent_listings': random_rent_listings,
        'listings': random_listings
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/index.html', context)


def buy(request):
    # переменные для отображения состояния фильтров
    vars_filter = dict()

    # все обьекты недвижимости для продажи
    all_listings = Listing.sell_objects.all()

    # информация о собственной компании
    our_company = OurCompany.objects.all().first()

    # каталоги
    catalogs = Catalog.objects.all()

    # блог
    random_blog_articles = get_random(Article.objects.all(), OFFERS_IN_CAROUSEL)

    # типы валют
    currencies = [{'value': 'usd', 'title': '$'},
                  {'value': 'eur', 'title': '€'},
                  {'value': 'rub', 'title': '₽'}, ]

    # типы единиц измерения площади
    areas = [{'value': 'sq_m', 'title': 'sq. m'},
             {'value': 'sq_ft', 'title': 'sq. ft'}]

    # множество статусов продажи недвижимости (например, В продаже или Старт продаж)
    sales_status_types = sorted(set(all_listings.filter(sales_status_a_en__isnull=False).values_list('sales_status_a_en', flat=True).distinct()))

    # множество типов недвижимости (например, residential_complex или village)
    estate_types = sorted(set(all_listings.filter(type__isnull=False).values_list('type', flat=True).distinct()))

    # множество районов города
    districts = sorted(set(District.objects.filter(listing__in=all_listings).values_list('name', flat=True).distinct()))

    # множество удобств на обьекте недвижимости
    am = Amenity.objects.filter(listing__in=all_listings).values_list('en', 'ar', 'ru').distinct()
    amenities = [{'en': en, 'ar': ar, 'ru': ru, } for en, ar, ru in sorted(am)]

    # извлечение из базы данных максимальных и минимальных цен на объекты недвижимости
    listings_price = get_min_max_listings_prices(all_listings)

    # цены на объекты недвижимости
    prices = Price.objects.exclude(key__isnull=True).filter(listing__in=all_listings)

    # минимальная площадь обьекта недвижимости из базы данных
    listings_area_min_sq_m = prices.aggregate(Min('min_area_m2'))['min_area_m2__min']
    listings_area_min_sq_ft = prices.aggregate(Min('min_area_ft2'))['min_area_ft2__min']

    # максимальная площадь обьекта недвижимости из базы данных
    listings_area_max_sq_m = prices.aggregate(Max('max_area_m2'))['max_area_m2__max']
    listings_area_max_sq_ft = prices.aggregate(Max('max_area_ft2'))['max_area_ft2__max']

    # максимальное количество комнат обьекта недвижимости из базы данных
    func = lambda x: int(x[-1]) if x[-1].isdigit() else 0
    rooms = list(map(func, prices.values_list('key', flat=True).distinct()))
    if rooms:
        listings_max_rooms = max(rooms)
    else:
        listings_max_rooms = 0

    # отфильтрованные обьекты в соотвествии с заданными на странице фильтрами
    listings = listing_filter(request,
                              queryset=all_listings,
                              estate_types=estate_types,
                              districts=districts,
                              amenities=amenities,
                              sales_status_types=sales_status_types)

    # точки на карте для всех отфильтрованных обьектов недвижимости для продажи
    geo_context = geomap_context(listings, auto_zoom="20")

    # url для htmx подгрузки
    request_get = request.GET.copy()
    if 'page' in request_get:
        request_get['page'] = str(int(request_get['page']) + 1)
    else:
        request_get['page'] = '2'  # следующая страница
    htmx_url = request_get.urlencode()

    # разбиение обьектов на порции-страницы для отображения в виде списка
    page = request.GET.get('page')
    paginator = Paginator(listings, 8)
    paged_listings = paginator.get_page(page)

    # переменные для отображения состояния фильтров в начале страницы

    # текущие значения минимальной и максимальной цены в базовой валюте - долларах
    variables = {var: check_number_var(request.GET, var) for var in ['price_min', 'price_max']}
    vars_filter.update(variables)

    sales_status_types_choices = create_choices(request, sales_status_types, 'sales_status_types')
    estate_types_choices = create_choices(request, estate_types, 'estate_type')

    # переменные для отображения состояния фильтров в buy_big_modal_filter.html

    variables = {var: check_number_var(request.GET, var) for var in ['bedrooms_min', 'bedrooms_max']}
    vars_filter.update(variables)

    # текущие значения минимальной и максимальной цены в движках контрола цены
    variables = {var: check_number_var(request.GET, var) for var in
                 ['price_rub_min', 'price_rub_max', 'price_dollar_min', 'price_dollar_max', 'price_euro_min',
                  'price_euro_max']}
    vars_filter.update(variables)

    vars_filter['currency'] = check_str_var(request.GET, 'currency', currencies[0]['value'])
    vars_filter['area'] = check_str_var(request.GET, 'area', areas[0]['value'])
    vars_filter['area_min'] = check_str_var(request.GET, 'area_min', listings_area_min_sq_m)
    vars_filter['area_max'] = check_str_var(request.GET, 'area_max', listings_area_max_sq_m)
    vars_filter['fut_min'] = check_str_var(request.GET, 'fut_min', listings_area_min_sq_ft)
    vars_filter['fut_max'] = check_str_var(request.GET, 'fut_max', listings_area_max_sq_ft)
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

    # print('currency', request.GET.get('currency'))
    # print('area', request.GET.get('area'))
    # print('price_rub_min', request.GET.get('price_rub_min'))
    # print('price_rub_max', request.GET.get('price_rub_max'))
    print('price_dollar_min', request.GET.get('price_dollar_min'))
    print('price_dollar_max', request.GET.get('price_dollar_max'))
    # print('price_euro_min', request.GET.get('price_euro_min'))
    # print('price_euro_max', request.GET.get('price_euro_max'))
    # print('area_min', request.GET.get('area_min'))
    # print('area_max', request.GET.get('area_max'))
    # print('fut_min', request.GET.get('fut_min'))
    # print('fut_max', request.GET.get('fut_max'))

    districts_choices = create_choices(request, districts, 'district')
    amenities_choices = create_choices(request, amenities, 'amenity', with_language_code=True)


    print(vars_filter)

    context = {
        'our_company': our_company,
        'catalogs': catalogs,
        'blog_articles': random_blog_articles,
        'len_listings': len(listings),
        # 'rent_listings': paged_rent_listings,
        'listings': paged_listings,
        'currencies': currencies,
        'areas': areas,
        'estate_types_choices': estate_types_choices,
        'districts_choices': districts_choices,
        'sales_status_types_choices': sales_status_types_choices,
        'amenities_choices': amenities_choices,
        'vars_filter': vars_filter,
        'htmx_url': htmx_url,
    }

    # print(geo_context)
    context.update(geo_context)
    if is_htmx(request):
        return render(request,
                      "includes/buy/buy_loaded_block.html",
                      {"listings": paged_listings,
                       'len_listings': len(listings),
                       'htmx_url': htmx_url,
                       }
                      )
    return render(request, 'includes/content/buy.html', context)


def arenda(request):
    # переменные для отображения состояния фильтров
    vars_filter = dict()

    # все обьекты недвижимости для аренды
    all_listings = Listing.rent_objects.all()

    # информация о собственной компании
    our_company = OurCompany.objects.all().first()

    # блог
    random_blog_articles = get_random(Article.objects.all(), OFFERS_IN_CAROUSEL)

    # типы валют
    currencies = [{'value': 'usd', 'title': '$'},
                  {'value': 'eur', 'title': '€'},
                  {'value': 'rub', 'title': '₽'}, ]

    # множество типов недвижимости (например, residential_complex или village)
    estate_types = sorted(set(all_listings.filter(type__isnull=False).values_list('type', flat=True).distinct()))

    # множество Подходит_для (1, 2, 3, более гостей)
    suitable_for = tuple(item for _, item in SUITABLE_FOR_CHOICES)

    # множество районов города
    districts = sorted(set(District.objects.filter(listing__in=all_listings).values_list('name', flat=True).distinct()))

    # множество типов апартаментов
    apartment_types = sorted(set(all_listings.values_list('apartment_type', flat=True).distinct()))

    # множество удобств на обьекте недвижимости
    am = Amenity.objects.filter(listing__in=all_listings).values_list('en', 'ar', 'ru').distinct()
    amenities = [{'en': en, 'ar': ar, 'ru': ru, } for en, ar, ru in sorted(am)]

    # извлечение из базы данных максимальных и минимальных цен на объекты недвижимости
    # для задания границ в движках контрола
    listings_price = get_min_max_listings_prices(all_listings)

    # отфильтрованные обьекты в соотвествии с заданными на странице фильтрами
    listings = listing_filter(request,
                              queryset=all_listings,
                              estate_types=estate_types,
                              apartment_types=apartment_types,
                              districts=districts,
                              amenities=amenities)

    # точки на карте для всех отфильтрованных обьектов недвижимости для продажи
    geo_context = geomap_context(listings, auto_zoom="20")

    # url для htmx подгрузки
    request_get = request.GET.copy()
    if 'page' in request_get:
        request_get['page'] = str(int(request_get['page']) + 1)
    else:
        request_get['page'] = '2'  # следующая страница
    htmx_url = request_get.urlencode()

    # разбиение обьектов на порции-страницы для отображения в виде списка
    page = request.GET.get('page')
    paginator = Paginator(listings, 6)
    paged_listings = paginator.get_page(page)

    # переменные для отображения состояния фильтров в начале страницы
    vars_filter['check_in'] = check_str_var(request.GET, 'check_in', ' ')
    vars_filter['check_out'] = check_str_var(request.GET, 'check_out', ' ')
    vars_filter['guest'] = check_str_var(request.GET, 'guest', suitable_for[0])

    # переменные для отображения состояния фильтров в rent_big_modal_filter.html

    # текущие значения минимальной и максимальной цены в базовой валюте - долларах
    variables = {var: check_number_var(request.GET, var) for var in ['price_min', 'price_max']}
    vars_filter.update(variables)

    estate_types_choices = create_choices(request, estate_types, 'estate_type')
    apartment_types_choices = create_choices(request, apartment_types, 'apartment_type')
    districts_choices = create_choices(request, districts, 'district')
    amenities_choices = create_choices(request, amenities, 'amenity', with_language_code=True)

    # текущие значения минимальной и максимальной цены в движках контрола цены
    variables = {var: check_number_var(request.GET, var) for var in
                 ['price_rub_min', 'price_rub_max', 'price_dollar_min', 'price_dollar_max', 'price_euro_min',
                  'price_euro_max']}
    vars_filter.update(variables)

    vars_filter['currency'] = check_str_var(request.GET, 'currency', currencies[0]['value'])

    # значения минимальной и максимальной цены в движках контрола цены,
    # максимальные и минимальные площади обьектов,
    # максимальное количество комнат
    variables = {'listings_price_min_aed': listings_price['min']['AED'],
                 'listings_price_min_usd': listings_price['min']['USD'],
                 'listings_price_min_eur': listings_price['min']['EUR'],
                 'listings_price_min_rub': listings_price['min']['RUB'],
                 'listings_price_max_aed': listings_price['max']['AED'],
                 'listings_price_max_usd': listings_price['max']['USD'],
                 'listings_price_max_eur': listings_price['max']['EUR'],
                 'listings_price_max_rub': listings_price['max']['RUB'],
                 }
    vars_filter.update(variables)

    context = {
        'our_company': our_company,
        'blog_articles': random_blog_articles,
        'len_listings': len(listings),
        'listings': paged_listings,
        'currencies': currencies,
        'estate_types_choices': estate_types_choices,
        'apartment_types_choices': apartment_types_choices,
        'districts_choices': districts_choices,
        'amenities_choices': amenities_choices,
        'vars_filter': vars_filter,
        'htmx_url': htmx_url,
        'suitable_for': suitable_for,
    }

    context.update(geo_context)

    if is_htmx(request):
        return render(request,
                      "includes/rent/rent_loaded_block.html",
                      {"listings": paged_listings,
                       'len_listings': len(listings),
                       'htmx_url': htmx_url,
                       }
                      )
    return render(request, 'includes/content/arenda.html', context)


def izbrannoe(request):
    user = auth.get_user(request)

    favorites = user.profile.favorites.all()
    geo_context = geomap_context(favorites, auto_zoom="20")

    listings = favorites.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')
    rent_listings = favorites.order_by('-list_date').filter(is_fully_loaded=True, offer_type='rent')

    our_company = OurCompany.objects.all().first()

    random_blog_articles = get_random(Article.objects.all(), OFFERS_IN_CAROUSEL)

    context = {
        'our_company': our_company,
        'listings': listings,
        'rent_listings': rent_listings,
        'blog_articles': random_blog_articles,
    }
    context.update(geo_context)
    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/izbrannoe.html', context)


def sravnenie(request):
    user = auth.get_user(request)

    bookmarks = user.profile.bookmarks.all()
    listings = bookmarks.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')
    geo_context = geomap_context(listings, auto_zoom="20")

    our_company = OurCompany.objects.all().first()
    catalogs = Catalog.objects.all()

    random_blog_articles = get_random(Article.objects.all(), OFFERS_IN_CAROUSEL)

    context = {
        'our_company': our_company,
        'catalogs': catalogs,
        'listings': listings,
        'blog_articles': random_blog_articles,
    }
    context.update(geo_context)
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


def policy(request):
    our_company = OurCompany.objects.all().first()
    context = {
        'our_company': our_company,
    }

    return render(request, 'includes/content/policy.html', context)


def otmena(request):
    our_company = OurCompany.objects.all().first()
    context = {
        'our_company': our_company,
    }

    return render(request, 'includes/content/otmena.html', context)


def lk(request):
    our_company = OurCompany.objects.all().first()
    context = {
        'our_company': our_company,
    }

    return render(request, 'includes/content/lk.html', context)

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
