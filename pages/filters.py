from functools import reduce
import operator

from django.utils.translation import gettext_lazy as _
from django.db.models import Q

from listings.models import SUITABLE_FOR_CHOICES
from pages.utils import check_number_var, check_str_var


def listing_filter(request,
                   queryset,
                   estate_types=None,
                   apartment_types=None,
                   districts=None,
                   amenities=None,
                   sales_status_types=None):

    # фильтрация по типу недвижимости (вилла, жилой комплекс и так далее)
    if estate_types:
        filters = list(Q(type=estate_type) for estate_type in estate_types if request.GET.get('estate_type_' + estate_type))
        if filters:
            q = reduce(operator.or_, filters)
            queryset = queryset.filter(q)

    # фильтрация по статусу продажи
    if sales_status_types:
        filters = list(Q(sales_status_a_en=sales_status_type) for sales_status_type in sales_status_types if request.GET.get('sales_status_type_' + sales_status_type))
        if filters:
            q = reduce(operator.or_, filters)
            queryset = queryset.filter(q)

    # фильтрация по типу объекта недвижимости (1 спальня, 2 спальни, пентхаус и так далее)
    if apartment_types:
        filters = list(Q(apartment_type=apartment_type) for apartment_type in apartment_types if request.GET.get('apartment_type_' + apartment_type))
        if filters:
            q = reduce(operator.or_, filters)
            queryset = queryset.filter(q)

    # фильтрация по району
    if districts:
        filters = list(Q(districts__name=district) for district in districts if request.GET.get('district_' + district))
        if filters:
            q = reduce(operator.or_, filters)
            queryset = queryset.filter(q)

    # фильтрация по удобствам
    if amenities:
        # query_specifier = {'amenity__' + language_code: 'amenity'}
        # filters = list(Q(**query_specifier) for amenity in amenities if request.GET.get(amenity))
        filters = list(Q(amenities__en=amenity['en']) for amenity in amenities if request.GET.get('amenity_' + amenity['en']))
        if filters:
            q = reduce(operator.or_, filters)
            queryset = queryset.filter(q)

    # фильтрация по максимальному количеству гостей
    guest = check_str_var(request.GET, 'guest')
    if guest:
        n_guest = 0
        for number, item in SUITABLE_FOR_CHOICES:
            if _(item) == guest:
                n_guest = number
                break
        q = Q(suitable_for__gte=n_guest)
        queryset = queryset.filter(q)

    # фильтрация по стоимости в базовой валюте (долларах)
    price_min_usd = check_number_var(request.GET, 'price_dollar_min', result_type_str=False)
    price_max_usd = check_number_var(request.GET, 'price_dollar_max', result_type_str=False)
    if price_max_usd:
        if price_min_usd:
            q = Q(price_min_usd__gte=price_min_usd) & Q(price_min_usd__lte=price_max_usd)
        else:
            q = Q(price_min_usd__lte=price_max_usd)
    else:
        if price_min_usd:
            q = Q(price_min_usd__gte=price_min_usd)
        else:
            q = None
    if q:
        queryset = queryset.filter(q)

    # фильтрация по количеству комнат
    bedrooms_min = check_number_var(request.GET, 'bedrooms_min', result_type_str=False)
    bedrooms_max = check_number_var(request.GET, 'bedrooms_max', result_type_str=False)
    if bedrooms_min and bedrooms_max:
        q = Q(prices__rooms__gte=bedrooms_min) & Q(prices__rooms__lte=bedrooms_max)
        if q:
            queryset = queryset.filter(q)

    # фильтрация по общей площади
    area_min = check_number_var(request.GET, 'area_min', result_type_str=False)
    area_max = check_number_var(request.GET, 'area_max', result_type_str=False)
    if area_min and area_max:
        q = Q(prices__min_area_m2__gte=area_min) & Q(prices__min_area_m2__lte=area_max)
        if q:
            queryset = queryset.filter(q)

    return queryset.distinct()
