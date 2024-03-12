from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from django.http import HttpResponseRedirect
from django.urls import path

# from loader.scan_for_developers import scan_developers
from .models import Listing, Bookmark, Favorite, Price

TokenAdmin.raw_id_fields = ['user']


class PriceInline(admin.TabularInline):
    model = Price


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

    change_list_template = "admin/model_change_list.html"

    inlines = [
        PriceInline,
    ]

    def get_urls(self):
        urls = super(ListingAdmin, self).get_urls()
        custom_urls = [path('import/', self.process_import, name='process_import'), ]
        return custom_urls + urls

    def process_import(self, request):
        # import_custom = ImportCustom()
        # count = import_custom.import_data()
        count = 0
        if 'airbnb' in request.POST:
            pass

        elif 'alnair' in request.POST:
            pass

        elif 'developers' in request.POST:
            # count = scan_developers()
            for price in Price.objects.all():
                price.rooms = int(price.key[-1]) if price.key[-1].isdigit() else 0
                price.save()
            pass

        self.message_user(request, f"создано {count} новых записей")
        return HttpResponseRedirect("../")


admin.site.register(Listing, ListingAdmin)
# admin.site.register(Listing.sell_objects.all(), ListingAdmin)
# admin.site.register(Listing.rent_objects.all(), ListingAdmin)
# admin.site.register(Bookmark)
# admin.site.register(Favorite)
