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
