from django.db import models
from tinymce.models import HTMLField
from listings.models import Listing
from realtors.models import Realtor


class Developer(models.Model):
    developer_a_title_a_ru = models.TextField(blank=True, null=True)
    developer_a_title_a_en = models.TextField(blank=True, null=True)
    developer_a_title_a_ar = models.TextField(blank=True, null=True)
    developer_a_logo = models.TextField(blank=True, null=True)

    year_of_foundation = models.TextField(max_length=4, blank=True, null=True)

    buildings_finished = models.IntegerField(blank=True, null=True)
    complexes_finished = models.IntegerField(blank=True, null=True)
    buildings_in_progress = models.IntegerField(blank=True, null=True)
    complexes_in_progress = models.IntegerField(blank=True, null=True)
    main_office = models.TextField(blank=True, null=True)
    number_of_employees = models.IntegerField(blank=True, null=True)
    stock_valuation = models.IntegerField(blank=True, null=True)

    text_en = HTMLField()
    text_ru = HTMLField()
    text_ar = HTMLField()

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    listings = models.ManyToManyField(Listing, related_name='listed_by')

    class Meta:
        verbose_name = 'Developer'
        verbose_name_plural = 'Developers'
        ordering = ['-id']
        db_table = "developers"

    def __str__(self):
        return self.developer_a_title_a_en
