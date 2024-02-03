import itertools

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from django_admin_geomap import geomap_context
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing, District, Amenity
from pages.filters import buy_listing_filter
from realtors.models import Realtor
from our_company.models import OurCompany


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

    context = {
        'our_company': our_company,
        'range': range(9),
        'blog_range': range(3),
        'rent_listings': paged_rent_listings,
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/index.html', context)


def buy(request):
    # информация о собственной компании
    our_company = OurCompany.objects.all().first()

    # множество типов недвижимости (например, residential_complex или village)
    estate_types = list(sorted(Listing.objects.values_list('type', flat=True).distinct()))
    # множество районов города
    districts = list(sorted(District.objects.values_list('name', flat=True).distinct()))
    # множество удобств на обьекте недвижимости
    am = Amenity.objects.values_list('en', 'ar', 'ru').distinct()
    amenities = [{'en': en, 'ar': ar, 'ru': ru, } for en, ar, ru in sorted(am)]

    # все обьекты недвижимости для продажи
    all_listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')
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


    # переменные для отображения состояния фильтров
    estate_types_choices = {estate_type: request.GET.get(estate_type) for estate_type in estate_types}
    if not any(estate_types_choices.values()):
        estate_types_choices = {estate_type: estate_type for estate_type in estate_types}

    districts_choices = {district: request.GET.get(district) for district in districts}
    if not any(districts_choices.values()):
        districts_choices = {district: district for district in districts}

    amenities_choices = {amenity['en']: request.GET.get(amenity['en']) for amenity in amenities}
    if not any(amenities_choices.values()):
        amenities_choices = {amenity['en']: amenity for amenity in amenities}

    vars_filter = {var: request.GET.get(var) for var in ['price_min', 'price_max']}

    context = {
        'our_company': our_company,
        'range': range(9),
        'blog_range': range(3),
        'len_listings': len(listings),
        'rent_listings': paged_rent_listings,
        'listings': paged_listings,
        'estate_types_choices': estate_types_choices,
        'districts_choices': districts_choices,
        'amenities_choices': amenities_choices,
        'vars_filter': vars_filter,
    }

    context.update(geo_context)

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/buy.html', context)


def arenda(request):
    listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='rent')

    our_company = OurCompany.objects.all().first()

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'our_company': our_company,
        'range': range(9),
        'blog_range': range(3),
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/arenda.html', context)


def izbrannoe(request):
    listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')

    our_company = OurCompany.objects.all().first()

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'our_company': our_company,
        'range': range(9),
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/izbrannoe.html', context)


def sravnenie(request):
    listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')

    our_company = OurCompany.objects.all().first()

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'our_company': our_company,
        'range': range(9),
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
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


def blog(request):
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

    return render(request, 'includes/content/blog.html', context)


def katalogi(request):
    our_company = OurCompany.objects.all().first()

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
        'range': range(9),
        'blog_range': range(3),
        'listings': paged_listings,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/katalogi.html', context)


def article(request):
    our_company = OurCompany.objects.all().first()
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
        'listings': paged_listings,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/article.html', context)


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
