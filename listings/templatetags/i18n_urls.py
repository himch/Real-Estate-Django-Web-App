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
    obj = context.get(obj_name, None)
    if obj:
        if hasattr(obj, attr_name):
            return getattr(obj, attr_name)
    return None
