def is_float(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


def is_int(s):
    try:
        int(s)
        return True
    except (ValueError, TypeError):
        return False


