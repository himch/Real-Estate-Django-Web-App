from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor


def index(request):
    page = request.GET.get('page')

    listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='sell')
    paginator = Paginator(listings, 6)
    paged_listings = paginator.get_page(page)

    rent_listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='rent')
    rent_paginator = Paginator(rent_listings, 6)
    paged_rent_listings = rent_paginator.get_page(page)

    context = {
        'rent_listings': paged_rent_listings,
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/index.html', context)


def buy(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='rent')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'range': range(9),
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/buy.html', context)


def arenda(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='rent')

    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'range': range(9),
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/arenda.html', context)


def izbrannoe(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'range': range(9),
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/izbrannoe.html', context)


def sravnenie(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'range': range(9),
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }

    # return render(request, 'pages/index.html', context)
    return render(request, 'includes/content/sravnenie.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/dadi.html', context)


def blog(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/blog.html', context)


def katalogi(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'includes/content/katalogi.html', context)


def article(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
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
#     listings = Listing.objects.order_by('-list_date').filter(is_published=True)
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
