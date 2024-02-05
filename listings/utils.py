def convert(value, currency1, currency2):
    courses = {'AEDRUB': 24.76,
               'AEDUSD': 0.27,
               'AEDEUR': 0.25,
               'AEDAED': 1,
               'RUBUSD': 0.011,
               'RUBEUR': 0.01,
               'RUBRUB': 1,
               }
    print('convert', value, currency1 + currency2)
    return int(round(value * courses[currency1 + currency2], -1))