from django import template

register = template.Library()


@register.filter
def user_in(objects, user):
	print(type(objects))
	print(objects)
	if user.is_authenticated:
		if hasattr(objects, 'filter'):
			return objects.filter(user=user).exists()
	return False
