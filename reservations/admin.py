from django.contrib import admin
from django import forms
from django.db.models.functions import Lower

from listings.models import Listing
from .models import Reservation
from djmoney.models.fields import MoneyField


class CustomReservationModelForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomReservationModelForm, self).__init__(*args, **kwargs)
        self.fields['listing'].queryset = Listing.objects.order_by('title_a_en').filter(is_fully_loaded=True, offer_type='rent')


class ReservationAdmin(admin.ModelAdmin):
    form = CustomReservationModelForm

    list_display = ['str_reservation']
    list_display_links = ['str_reservation']
    readonly_fields = ['created',
                       'price_per_month_currency',
                       'price_per_day_currency',
                       'cleaning_cost_currency',
                       'concierge_service_cost_currency']
    view_on_site = True

    def get_fields(self, request, obj=None):
        fields = [field.name for field in self.model._meta.concrete_fields  if field.name != "id"]
        return fields

    def str_reservation(self, instance):
        return str(instance)

    str_reservation.short_description = 'Reservations'


admin.site.register(Reservation, ReservationAdmin)
