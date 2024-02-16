import json
import ast
from functools import reduce
import operator
from typing import Union

from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import serializers


from rest_framework import generics, status
from rest_framework.response import Response

from our_company.models import OurCompany
from pages.utils import check_number_var
from .choices import price_choices, bedroom_choices, state_choices

from .models import Listing, Bookmark, Favorite
from .serializers import ListingSerializer, ListingFavoriteSerializer
from .utils import convert


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


class ListingAPIView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class OffersBuyAPIView(generics.GenericAPIView):
    # queryset = Listing.objects.all()
    # serializer_class = ListingSerializer

    # def get_queryset(self, *args, **kwargs):
    #     queryset = Listing.objects.all()
    #     return queryset

    def get(self, request, *args, **kwargs):
        try:

            price_min = check_number_var(request.query_params, 'price_min', result_type_str=False)
            price_max = check_number_var(request.query_params, 'price_max', result_type_str=False)
            estate_types = list(sorted(Listing.objects.values_list('type', flat=True).distinct()))
            filters = list(
                Q(type=estate_type) for estate_type in estate_types if
                'estate_type_' + estate_type in request.query_params)

            queryset = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')
            if filters:
                q = reduce(operator.or_, filters)
                queryset = queryset.filter(q)

            if price_max:
                q = Q(price_a_min__gte=price_min) & Q(price_a_min__lte=price_max)
            else:
                if price_min:
                    q = Q(price_a_min__gte=price_min)
                else:
                    q = None
            if q:
                queryset = queryset.filter(q)

            count = queryset.count()
            return Response({'count': count}, status=status.HTTP_200_OK)

        except Exception as e:
            print('Exception', e)
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    # def post(self, request):
    #     listing_data = request.data
    #     new_listing = Listing.objects.create(
    #         title=listing_data['title'],
    #     )
    #     new_listing.save()
    #
    #     serializer = ListingSerializer(new_listing)
    #     return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
    #     id = request.query_params["id"]
    #     listing_object = Listing.objects.get(id=id)
    #
    #     data = request.data
    #
    #     listing_object.title = data["title"]
    #     listing_object.save()
    #
    #     serializer = ListingSerializer(listing_object)
    #     return Response(serializer.data)

    # def patch(self, request, *args, **kwargs):
    #     id = request.query_params["id"]
    #     listing_object = Listing.objects.get(id=id)
    #
    #     data = request.data
    #
    #     listing_object.title = data.get('title', listing_object.title)
    #     listing_object.save()
    #     serializer = ListingSerializer(listing_object)
    #     return Response(serializer.data)


def listing(request, listing_id):
    our_company = OurCompany.objects.all().first()

    listing_item = get_object_or_404(Listing, pk=listing_id)
    bookmark = listing_item.bookmark_set.all
    print(bookmark)

    favorite = listing_item.favorite_set.all
    print(favorite)

    realtor = listing_item.realtor

    listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='sell')

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

    if listing_item.listing_amenities is not None:
        amenities = [amenity[request.LANGUAGE_CODE] for amenity in json.loads(listing_item.listing_amenities) if
                     request.LANGUAGE_CODE in amenity]
    else:
        amenities = None

    print(amenities)

    context = {
        'our_company': our_company,

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

        'amenities': amenities,

        'listing': listing_item,
        'listings': paged_listings,
        'realtor': realtor
    }

    # return render(request, 'listings/listing.html', context)
    return render(request, 'includes/content/jk.html', context)


def rent(request, listing_id):
    our_company = OurCompany.objects.all().first()

    listing_item = get_object_or_404(Listing, pk=listing_id)

    realtor = listing_item.realtor

    listings = Listing.objects.order_by('-list_date').filter(is_fully_loaded=True, offer_type='rent')

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

    if listing_item.listing_amenities is not None:
        amenities = [amenity[request.LANGUAGE_CODE] for amenity in json.loads(listing_item.listing_amenities) if
                     request.LANGUAGE_CODE in amenity]
    else:
        amenities = None

    print(amenities)

    context = {
        'our_company': our_company,

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

        'amenities_ru': amenities[:9],
        'amenities_en': amenities[:9],
        'amenities_ar': amenities[:9],
        'listing': listing_item,
        'listings': paged_listings,
        'realtor': realtor
    }

    # return render(request, 'listings/listing.html', context)
    return render(request, 'includes/content/arenda-single.html', context)


# POST /api/v1/offers/<int:listing_id>/bookmark/  - добавить/удалить обьект с указанным id в сравнение для текущего пользователя.
# Возвращает {"result": ['added' если добавлен, 'deleted' если удален, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в сравнении для данного пользователя или 0, если пользователь не авторизован]}
#
# GET /api/v1/offers/bookmarks/  - информация об обьектах в сравнении для текущего пользователя.
# Возвращает {"result": ['success' если успешно, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в сравнении для данного пользователя или 0, если пользователь не авторизован]}
#
# POST /api/v1/offers/<int:listing_id>/favorite/  - добавить/удалить обьект с указанным id в избранное для текущего пользователя.
# Возвращает {"result": ['added' если добавлен, 'deleted' если удален, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в избранном для данного пользователя или 0, если пользователь не авторизован]}
#
# GET /api/v1/offers/favorites/  - информация об обьектах в избранном для текущего пользователя.
# Возвращает {"result": ['success' если успешно, 'error' если ошибка или пользователь не авторизован],
# "count": [количество обьектов в избранном для данного пользователя или 0, если пользователь не авторизован]}


class BookmarkAPIView(generics.GenericAPIView):
    model = None

    def get_serializer_class(self):
        return ListingFavoriteSerializer

    def post(self, request, listing_id):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            bookmark, created = self.model.objects.get_or_create(user=user, listing_id=listing_id)
            if not created:
                bookmark.delete()

            if created:
                return Response(
                    {"result": 'added',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer added to {model._meta.verbose_name_plural.title()}'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"result": 'deleted',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer deleted from {self.model._meta.verbose_name_plural.title()}'},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"result": 'error',
                 "count": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )

    def get(self, request, listing_id):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            try:
                bookmark = self.model.objects.get(user=user, listing_id=listing_id).first
            except self.model.DoesNotExist:
                bookmark = None
            if bookmark:
                return Response(
                    {"result": 'bookmarked',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer bookmarked in {self.model._meta.verbose_name_plural.title()}'},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"result": 'not bookmarked',
                     "count": self.model.objects.filter(user=user).count(),
                     'message': f'Offer not bookmarked in {self.model._meta.verbose_name_plural.title()}'
                     },
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                {"result": 'error',
                 "count": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class BookmarksAPIView(generics.GenericAPIView):
    model = None

    def get(self, request):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            return Response(
                {"result": 'success',
                 "count": self.model.objects.filter(user=user).count(),
                 'message': f'All offers for current user in {self.model._meta.verbose_name_plural.title()}'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"result": 'error',
                 "count": 0,
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )


def search(request):
    our_company = OurCompany.objects.all().first()

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
        'our_company': our_company,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
