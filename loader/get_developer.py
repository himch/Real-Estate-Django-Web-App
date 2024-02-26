from random import choice


def developer_get_or_add(title_en, title_ru, title_ar, logo, Realtor, Developer):
    realtor_list = Realtor.objects.all()
    realtors_ids = [realtor.id for realtor in realtor_list]
    unknown_developer, created = Developer.objects.get_or_create(slug='unknown',
                                                                 defaults={'title_en': 'The Unknown',
                                                                           'title_ru': 'The Unknown',
                                                                           'title_ar': 'The Unknown',
                                                                           'logo': '/img/unknown.jpeg',
                                                                           'realtor_id': choice(realtors_ids)})

    titles = [title_en, title_ru, title_ar]
    titles = list(filter(None, titles))
    if titles:
        title_en = title_en if title_en else titles[0]
        title_ru = title_ru if title_ru else titles[0]
        title_ar = title_ar if title_ar else titles[0]
        developer, created = Developer.objects.get_or_create(title_en=title_en,
                                                             defaults={'title_en': title_en,
                                                                       'title_ru': title_ru,
                                                                       'title_ar': title_ar,
                                                                       'logo': logo,
                                                                       'realtor_id': choice(realtors_ids)})
    else:
        developer = unknown_developer
    return developer
