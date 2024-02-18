from django.core.paginator import Paginator


def check_number_var(get_object, var, result_type_str=True):
    result = get_object.get(var)
    if result is None:
        return '' if result_type_str else 0
    else:
        result = int(result) if result.isdigit() else 0
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
