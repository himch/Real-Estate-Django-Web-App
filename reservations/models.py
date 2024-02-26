from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator

from accounts.models import Profile
from listings.models import Listing
from realtors.models import Realtor

SHORT_TERM = 'SHORT-TERM'
MID_TERM = 'MID-TERM'
LONG_TERM = 'LONG-TERM'

RENTAL_CATEGORIES = [(LONG_TERM, 'Long-Term'),
                     (MID_TERM, 'Mid-Term'),
                     (SHORT_TERM, 'Short-Term')]


class Reservation(models.Model):
    client = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    rental_category = models.CharField(max_length=12, choices=RENTAL_CATEGORIES, default=MID_TERM)

    start_date = models.DateField(blank=True)

    price_per_month = MoneyField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default_currency='UDS',
        validators=[MinMoneyValidator(0)]
    )
    total_months = models.IntegerField(blank=True, null=True)

    price_per_day = MoneyField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default_currency='UDS',
        validators=[MinMoneyValidator(0)]
    )
    total_days = models.IntegerField(blank=True, null=True)

    numbers_of_cleanings = models.IntegerField(blank=True, null=True, default=2)
    cleaning_cost = MoneyField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default_currency='UDS',
        validators=[MinMoneyValidator(0)]
    )

    numbers_of_concierge_services = models.IntegerField(blank=True, null=True, default=2)
    concierge_service_cost = MoneyField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        default_currency='UDS',
        validators=[MinMoneyValidator(0)]
    )

    info = models.TextField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ['-id']
        db_table = "reservations"

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.listing.title_a_en}  👤{self.client.user.get_full_name()} - {self.rental_category} - {self.total_days if self.rental_category == SHORT_TERM else self.total_months} {"day(s)" if self.rental_category == SHORT_TERM else "month(s)"} - from {self.start_date}'
