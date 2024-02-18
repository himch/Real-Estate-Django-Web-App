from functools import reduce
import operator

from django.db.models import Q

from pages.utils import check_number_var


def buy_listing_filter(get_object, queryset, language_code, estate_types, districts, amenities):
    filters = list(Q(type=estate_type) for estate_type in estate_types if get_object.get('estate_type_' + estate_type))
    if filters:
        q = reduce(operator.or_, filters)
        queryset = queryset.filter(q)

    filters = list(Q(districts__name=district) for district in districts if get_object.get('district_' + district))
    if filters:
        q = reduce(operator.or_, filters)
        print(q)
        queryset = queryset.filter(q)

    # query_specifier = {'amenity__' + language_code: 'amenity'}
    # filters = list(Q(**query_specifier) for amenity in amenities if get_object.get(amenity))
    filters = list(Q(amenities__en=amenity['en']) for amenity in amenities if get_object.get('amenity_' + amenity['en']))
    if filters:
        q = reduce(operator.or_, filters)
        queryset = queryset.filter(q)

    price_min = check_number_var(get_object, 'price_min', result_type_str=False)
    price_max = check_number_var(get_object, 'price_max', result_type_str=False)
    if price_max:
        q = Q(price_a_min__gte=price_min) & Q(price_a_min__lte=price_max)
    else:
        if price_min:
            q = Q(price_a_min__gte=price_min)
        else:
            q = None
    if q:
        queryset = queryset.filter(q)

    return queryset.distinct()
