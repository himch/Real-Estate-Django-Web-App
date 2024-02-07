from django import template
from django.urls import translate_url

register = template.Library()


@register.simple_tag(takes_context=True)
def change_lang(context, lang: str, *args, **kwargs):
    path = context['request'].path

    return translate_url(path, lang)


@register.simple_tag(takes_context=True)
def get_attr(context, obj_name: str, attr_name: str, *args, **kwargs):
    """ Returns the value of dynamic_var_name into the context """

    def safe_iterate_get(iterate_object, index, default):
        try:
            return iterate_object[index]
        except IndexError:
            return default

    obj = context.get(obj_name, None)
    if obj:
        for attr in attr_name.split('.'):
            if attr.isdigit():
                obj = safe_iterate_get(obj, int(attr), None)
            else:
                if hasattr(obj, attr):
                    obj = getattr(obj, attr)
                else:
                    return None
        return obj
    return None
