import json
import os
from urllib.request import urlopen
from urllib.parse import urlparse

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    # title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # zipcode = models.CharField(max_length=20)
    # description = models.TextField(blank=True)
    # price = models.IntegerField()
    # bedrooms = models.IntegerField()
    # bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    # garage = models.IntegerField(default=0)
    # sqft = models.IntegerField()
    # lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_main_thumbnail_width_750 = ImageSpecField(source='photo_main',
                                                    processors=[ResizeToFill(width=750, height=450, upscale=False)],
                                                    format='WEBP',
                                                    options={'quality': 100})
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    # photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True, blank=True)

    def _get_planned_completion(self):
        return self.planned_completion_at[:7]

    planned_completion = property(_get_planned_completion)

    # ---------------------------------------------------
    complex_id = models.IntegerField(null=True)
    type = models.TextField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    title_a_ru = models.TextField(blank=True, null=True)
    title_a_en = models.TextField(blank=True, null=True)
    title_a_ar = models.TextField(blank=True, null=True)
    description_a_ru = models.TextField(blank=True, null=True)
    description_a_en = models.TextField(blank=True, null=True)
    description_a_ar = models.TextField(blank=True, null=True)
    price_on_request = models.IntegerField(null=True)
    status_a_ru = models.TextField(blank=True, null=True)
    status_a_en = models.TextField(blank=True, null=True)
    status_a_ar = models.TextField(blank=True, null=True)
    construction_start_at = models.TextField(blank=True, null=True)
    construction_progress = models.FloatField(null=True)
    planned_completion_at = models.TextField(blank=True, null=True)
    predicted_completion_at = models.TextField(blank=True, null=True)
    listing_amenities = models.JSONField(blank=True, null=True)
    developer_a_title_a_ru = models.TextField(blank=True, null=True)
    developer_a_title_a_en = models.TextField(blank=True, null=True)
    developer_a_title_a_ar = models.TextField(blank=True, null=True)
    developer_a_logo = models.TextField(blank=True, null=True)
    districts = models.TextField(blank=True, null=True)
    # address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    listing_album = models.JSONField(blank=True, null=True)
    albums_a_title_a_ru = models.TextField(blank=True, null=True)
    albums_a_title_a_en = models.TextField(blank=True, null=True)
    albums_a_title_a_ar = models.TextField(blank=True, null=True)
    listing_albums_a_images = models.JSONField(blank=True, null=True)
    buildings_count = models.IntegerField(null=True)
    for_sale_count = models.IntegerField(null=True)
    price_a_min = models.IntegerField(null=True)
    price_a_max = models.IntegerField(null=True)
    price_a_currency = models.TextField(blank=True, null=True)
    listing_br_prices = models.JSONField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    is_sold_out = models.IntegerField(null=True)
    payment_plans_a_title_a_ru = models.TextField(blank=True, null=True)
    payment_plans_a_title_a_en = models.TextField(blank=True, null=True)
    payment_plans_a_title_a_ar = models.TextField(blank=True, null=True)
    payment_plans_a_on_booking_percent = models.IntegerField(null=True)
    payment_plans_a_on_booking_fix = models.TextField(blank=True, null=True)
    payment_plans_a_on_construction_percent = models.IntegerField(null=True)
    payment_plans_a_on_construction_fix = models.TextField(blank=True, null=True)
    payment_plans_a_on_construction_payments_count = models.IntegerField(null=True)
    payment_plans_a_on_handover_percent = models.TextField(blank=True, null=True)
    payment_plans_a_on_handover_fix = models.TextField(blank=True, null=True)
    payment_plans_a_on_handover_payments_count = models.IntegerField(null=True)
    payment_plans_a_post_handover_percent = models.TextField(blank=True, null=True)
    payment_plans_a_post_handover_fix = models.TextField(blank=True, null=True)
    payment_plans_a_on_post_handover_payments_count = models.IntegerField(null=True)
    payment_plans_a_additional_a_title_a_ru = models.TextField(blank=True, null=True)
    payment_plans_a_additional_a_title_a_en = models.TextField(blank=True, null=True)
    payment_plans_a_additional_a_title_a_ar = models.TextField(blank=True, null=True)
    payment_plans_a_additional_a_percent = models.IntegerField(null=True)
    payment_plans_a_additional_a_fix = models.TextField(blank=True, null=True)
    payment_plans_a_additional_percent = models.IntegerField(null=True)
    payment_plans_a_additional_fix = models.IntegerField(null=True)
    payment_plans_a_roi_percent = models.TextField(blank=True, null=True)
    payment_plans_a_roi_fix = models.TextField(blank=True, null=True)
    payment_plans_a_roi_payments_count = models.IntegerField(null=True)
    payment_plans_a_currency = models.TextField(blank=True, null=True)
    payment_plans_a_period_after_handover_a_period = models.TextField(blank=True, null=True)
    payment_plans_a_period_after_handover_a_count = models.TextField(blank=True, null=True)
    payment_plans_a_period_after_handover_a_repeat_count = models.TextField(blank=True, null=True)
    payment_plans_a_period_after_roi_a_period = models.TextField(blank=True, null=True)
    payment_plans_a_period_after_roi_a_count = models.TextField(blank=True, null=True)
    payment_plans_a_period_after_roi_a_repeat_count = models.TextField(blank=True, null=True)
    sales_status_a_ru = models.TextField(blank=True, null=True)
    sales_status_a_en = models.TextField(blank=True, null=True)
    sales_status_a_ar = models.TextField(blank=True, null=True)
    listing_stocks = models.JSONField(blank=True, null=True)
    eoi_a_is_eoi_return = models.TextField(blank=True, null=True)
    eoi_a_eoi_items = models.TextField(blank=True, null=True)
    service_charge = models.TextField(blank=True, null=True)
    assignment = models.TextField(blank=True, null=True)

    def save_image_from_url(self, url, image_field):
        path = urlparse(url).path
        ext = os.path.splitext(path)[1]
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        image_field.save(f"image_{self.complex_id}" + ext, File(img_temp))

    def get_image_from_url(self):
        if self.photo and not self.photo_main:
            self.save_image_from_url(self.photo, self.photo_main)
            # path = urlparse(self.photo).path
            # ext = os.path.splitext(path)[1]
            # img_temp = NamedTemporaryFile(delete=True)
            # img_temp.write(urlopen(self.photo).read())
            # img_temp.flush()
            # self.photo_main.save(f"image_{self.complex_id}" + ext, File(img_temp))
        photos = json.loads(self.listing_album)
        if len(photos) >= 1:
            if not self.photo_1:
                self.save_image_from_url(photos[0], self.photo_1)
        if len(photos) >= 2:
            if not self.photo_2:
                self.save_image_from_url(photos[1], self.photo_2)
        if len(photos) >= 3:
            if not self.photo_3:
                self.save_image_from_url(photos[2], self.photo_3)
        if len(photos) >= 4:
            if not self.photo_4:
                self.save_image_from_url(photos[3], self.photo_4)

    def save(self, **kwargs):
        # do_something()
        self.get_image_from_url()
        super().save(**kwargs)  # Call the "real" save() method.
        # do_something_else()

    def __str__(self):
        return self.title_a_en
