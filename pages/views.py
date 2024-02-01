from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from functools import reduce
import operator

from django_admin_geomap import geomap_context
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing, District, Amenity
from realtors.models import Realtor
from our_company.models import OurCompany


def listing_filter(get_object, queryset, offer_types):
    filters = list(Q(type=offer_type) for offer_type in offer_types if get_object.get(offer_type))
    if filters:
        q = reduce(operator.or_, filters)
        print(q)
        queryset = queryset.filter(q)

    price_min = get_object.get('price_min') if get_object.get('price_min') else 0
    price_max = get_object.get('price_max')
    if price_max:
        q = Q(price_a_min__gte=price_min) & Q(price_a_min__lte=price_max)
    else:
        q = Q(price_a_min__gte=price_min)
    result = queryset.filter(q)
    return result


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
    page = request.GET.get('page')

    our_company = OurCompany.objects.all().first()

    offer_types = sorted(Listing.objects.values_list('type', flat=True).distinct())
    districts = sorted(District.objects.values_list('name', flat=True).distinct())
    amenities = sorted(Amenity.objects.values_list(request.LANGUAGE_CODE, flat=True).distinct())

    all_listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')
    listings = listing_filter(request.GET, queryset=all_listings, offer_types=offer_types)

    paginator = Paginator(listings, 6)
    paged_listings = paginator.get_page(page)

    rent_listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='rent')
    rent_paginator = Paginator(rent_listings, 6)
    paged_rent_listings = rent_paginator.get_page(page)

    geo_context = geomap_context(listings, auto_zoom="20")

    offer_types_choices = {offer_type: request.GET.get(offer_type) for offer_type in offer_types}
    if not any(offer_types_choices.values()):
        offer_types_choices = {offer_type: offer_type for offer_type in offer_types}

    districts_choices = {district: request.GET.get(district) for district in districts}
    if not any(districts_choices.values()):
        districts_choices = {district: district for district in districts}

    amenities_choices = {amenity: request.GET.get(amenity) for amenity in amenities}
    if not any(amenities_choices.values()):
        amenities_choices = {amenity: amenity for amenity in amenities}

    vars_filter = {var: request.GET.get(var) for var in ['price_min', 'price_max']}

    context = {
        'our_company': our_company,
        'range': range(9),
        'blog_range': range(3),
        'rent_listings': paged_rent_listings,
        'listings': paged_listings,
        'offer_types_choices': offer_types_choices,
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
