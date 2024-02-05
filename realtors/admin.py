from django.contrib import admin

from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_en', 'email', 'hire_date')
    list_display_links = ('id', 'name_en')
    search_fields = ('name_en',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
