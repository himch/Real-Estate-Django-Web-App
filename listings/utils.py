import json


def convert(value, currency1, currency2):
    courses = {'AEDRUB': 24.76,
               'AEDUSD': 0.27,
               'AEDEUR': 0.25,
               'AEDAED': 1,

               'RUBUSD': 0.011,
               'RUBEUR': 0.01,
               'RUBRUB': 1,
               'RUBAED': 0.004,

               'USDRUB': 92.5,
               'USDUSD': 1,
               'USDEUR': 0.93,
               'USDAED': 3.67,

               'EURUSD': 1.08,
               'EUREUR': 1,
               'EURRUB': 99.67,
               'EURAED': 3.96,
               }
    print('convert', value, currency1 + currency2)
    return int(round(value * courses[currency1 + currency2], -1))


def fix_description(text: str):
    run = True
    while run:
        if text is None:
            break
        len_old = len(text)
        text = text.replace('<p></p>', '')
        run = len_old != len(text)
    return text


def json_equal(a, b):
    if a is None or b is None:
        # print('a', a)
        # print('b', b)
        # print('a is None or b is None')
        return a == b
    try:
        obj_a = json.loads(a)
        obj_b = json.loads(b)
        # print('obj_a', obj_a)
        # print('obj_b', obj_b)
        # print('obj_a == obj_b', obj_a == obj_b)
    except json.decoder.JSONDecodeError:
        # print('a', a)
        # print('b', b)
        # print('json.decoder.JSONDecodeError')
        return a == b

    return obj_a == obj_b

