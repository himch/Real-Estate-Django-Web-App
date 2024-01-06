from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display = ('id',
                    'complex_id',
                    'title_a_ru',
                    'title_a_en',
                    'title_a_ar',
                    'is_published',
                    'price_a_min',
                    'list_date',
                    'realtor')
    # list_display_links = ('id',
    #                       'title')
    list_display_links = ('id',
                          'complex_id',
                          'title_a_ru',
                          'title_a_en',
                          'title_a_ar')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title_a_ru',
                     'title_a_en',
                     'title_a_ar',
                     'description_a_ru',
                     'description_a_en',
                     'description_a_ar',
                     'address',
                     'price_a_min')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
