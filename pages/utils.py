from django.core.paginator import Paginator
from django.db.models import Min, Max
from listings.utils import convert


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def get_min_max_listings_prices(listings):
    # извлечение из базы данных максимальных и минимальных цен на объекты недвижимости
    # для задания границ в движках контрола

    listings_price = dict()
    listings_price['min'] = dict()
    listings_price['max'] = dict()
    # {'min':
    # {'AED': 9410, 'RUB': 232990, 'USD': 2540, 'EUR': 2350},
    # 'max':
    # {'AED': 330206740, 'RUB': 8175918880, 'USD': 89155820, 'EUR': 82551680}}

    # минимальная цена объекта недвижимости из базы данных
    for currency in ['AED', 'RUB', 'USD', 'EUR']:
        listings_price['min'][currency] = listings.filter(price_a_currency=currency).aggregate(Min('price_a_min'))[
            'price_a_min__min']
        listings_price['max'][currency] = listings.filter(price_a_currency=currency).aggregate(Max('price_a_min'))[
            'price_a_min__max']

    # print('prices', listings_price)

    min_prices = []
    for currency, value in listings_price['min'].items():
        if value:
            min_prices.append(convert(value, currency, 'USD'))
    min_price_usd = min(min_prices) * 0.9 if min_prices else None

    max_prices = []
    for currency, value in listings_price['max'].items():
        if value:
            max_prices.append(convert(value, currency, 'USD'))
    max_price_usd = min(max_prices) * 1.1 if max_prices else None

    for currency in ['AED', 'RUB', 'USD', 'EUR']:
        listings_price['min'][currency] = convert(min_price_usd, 'USD', currency)
        listings_price['max'][currency] = convert(max_price_usd, 'USD', currency)

    # print('prices', listings_price)
    return listings_price


def create_choices(request, items, items_name, with_language_code=False):
    if with_language_code:
        choices = {items_name + '_' + item['en']:
                       {'value': request.GET.get(items_name + '_' + item['en']),
                        'title': item[request.LANGUAGE_CODE]}
                   for item in items}
        if not any(value['value'] for value in choices.values()):
            choices = {items_name + '_' + item['en']:
                           {'value': item['en'],
                            'title': item[request.LANGUAGE_CODE]}
                       for item in items}
    else:
        choices = {items_name + '_' + item:
                       {'value': request.GET.get(items_name + '_' + item),
                        'title': item}
                   for item in items}
        if not any(value['value'] for value in choices.values()):
            choices = {items_name + '_' + item:
                           {'value': item,
                            'title': item}
                       for item in items}
    return choices


def check_number_var(get_object, var, result_type_str=True):
    result = get_object.get(var)
    if result is None:
        return '' if result_type_str else 0
    else:
        result = int(float(result)) if is_float(result) else 0
        if result_type_str:
            return str(result) if result else ''
        else:
            return result


def check_str_var(get_object, var, default=None):
    result = get_object.get(var)
    if result is None:
        if default:
            return default
    else:
        return result


def is_htmx(request, boost_check=True):
    hx_boost = request.headers.get("Hx-Boosted")
    hx_request = request.headers.get("Hx-Request")
    if boost_check and hx_boost:
        return False

    elif boost_check and not hx_boost and hx_request:
        return True


def paginate(request, qs, limit=6):
    paginated_qs = Paginator(qs, limit)
    page_no = request.GET.get("page")
    return paginated_qs.get_page(page_no)
