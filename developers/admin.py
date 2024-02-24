from django.contrib import admin
from django.db.models.functions import Lower

from .models import Developer


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'get_listings']
    list_display_links = ['title_en']

    readonly_fields = ['image_logo']

    view_on_site = True

    def get_fields(self, request, obj=None):
        fields = [field.name for field in self.model._meta.concrete_fields  if field.name != "id"]
        try:
            logo_index = fields.index('logo') + 1
        except ValueError:
            logo_index = len(fields)
        fields.insert(logo_index, 'image_logo')
        return fields

    def get_listings(self, instance):
        return [listing.title_a_en for listing in instance.listing_set.all()]

    get_listings.short_description = 'Residential complexes by developer'

    def get_ordering(self, request):
        return [Lower('title_en')]


admin.site.register(Developer, DeveloperAdmin)
