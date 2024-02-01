import json
import os
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import URLError

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from datetime import datetime
from django_admin_geomap import GeoItem

from modules.services.utils import say_my_name
from realtors.models import Realtor


# class User(AbstractUser):
#     mobile = models.CharField(max_length=30, blank=True)


class Listing(models.Model, GeoItem):
    source = models.TextField(default='alnair')
    offer_type = models.TextField(default='sell')
    url = models.URLField(blank=True, null=True)
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
        if self.planned_completion_at:
            return self.planned_completion_at[:7]
        else:
            return None

    planned_completion = property(_get_planned_completion)

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

    special_price = models.IntegerField(blank=True, null=True, default=1)

    price_on_request = models.IntegerField(blank=True, null=True)

    status_a_ru = models.TextField(blank=True, null=True)
    status_a_en = models.TextField(blank=True, null=True)
    status_a_ar = models.TextField(blank=True, null=True)

    construction_start_at = models.TextField(blank=True, null=True)
    construction_progress = models.FloatField(null=True)
    planned_completion_at = models.TextField(blank=True, null=True)
    predicted_completion_at = models.TextField(blank=True, null=True)

    developer_a_title_a_ru = models.TextField(blank=True, null=True)
    developer_a_title_a_en = models.TextField(blank=True, null=True)
    developer_a_title_a_ar = models.TextField(blank=True, null=True)
    developer_a_logo = models.TextField(blank=True, null=True)

    listing_amenities = models.JSONField(blank=True, null=True)
    listing_districts = models.JSONField(blank=True, null=True)

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    is_fully_loaded = models.BooleanField(default=False)

    @property
    def geomap_longitude(self):
        return '' if self.longitude is None else str(self.longitude)

    @property
    def geomap_latitude(self):
        return '' if self.latitude is None else str(self.latitude)

    @property
    def geomap_popup_view(self):
        html_code = "<a href='/listings/" + str(self.pk) + "'>"
        html_code += "<div class='p-card__top flex'>"
        html_code += "<div class='p-card__top-left text-c5'>"
        html_code += str(self)
        html_code += "</div></div>"
        html_code += "<img src='" + str(self.photo_main.url if self.photo_main else None) + "' alt='' loading='lazy' />"
        html_code += "</a>"
        if self.sales_status_a_en:
            html_code += "<div class='p-card__price text-500'>"
            html_code += _(self.sales_status_a_en)
            html_code += "</div>"
        if self.price_a_min:
            html_code += "<div class='p-card__price text-500'>"
            html_code += _('from') + ' ' + f"{self.price_a_min:_}".replace("_", " ") + ' ' + str(self.price_a_currency)
            html_code += "</div>"
        if self.status_a_en:
            html_code += "<div class='p-card__price text-500'>"
            html_code += _(self.status_a_en)
            html_code += "</div>"
        # print(str(self.photo_main.url if self.photo_main else None))
        return html_code

    @property
    def geomap_icon(self):
        return self.default_icon

    # function
    # setMarker(coordinate, info_html, icon)
    # {
    #     var
    # marker = new
    # ol.Feature({
    #     geometry: new ol.geom.Point(ol.proj.fromLonLat(coordinate)),
    #     name: info_html,
    # });
    # var
    # iconBlue = new
    # ol.style.Style({
    #     image: new ol.style.Icon({
    #         anchor: [12, 40],
    #         anchorXUnits: 'pixels',
    #         anchorYUnits: 'pixels',
    #         opacity: 1,
    #         src: icon
    #     }),
    #     text: new
    # ol.style.Text({
    #     text: "",
    #     scale: 1.2,
    #     fill: new ol.style.Fill({
    #         color: "#fff"
    #     }),
    #     stroke: new
    # ol.style.Stroke({
    #     color: "0",
    #     width: 3
    # })
    # })
    # });
    # // marker.setStyle(styles.get(icon));
    # marker.setStyle(iconBlue);
    # vectorSource.addFeature(marker);
    # return marker;
    # }

    listing_album = models.JSONField(blank=True, null=True)
    listing_albums = models.JSONField(blank=True, null=True)

    buildings_count = models.IntegerField(null=True)
    for_sale_count = models.IntegerField(null=True)

    price_a_min = models.IntegerField(null=True)
    price_a_max = models.IntegerField(null=True)
    price_a_currency = models.TextField(blank=True, null=True)

    listing_br_prices = models.JSONField(blank=True, null=True)

    updated_at = models.TextField(blank=True, null=True)

    is_sold_out = models.IntegerField(null=True)
    listing_payment_plans = models.JSONField(blank=True, null=True)

    sales_status_a_ru = models.TextField(blank=True, null=True)
    sales_status_a_en = models.TextField(blank=True, null=True)
    sales_status_a_ar = models.TextField(blank=True, null=True)

    listing_stocks = models.JSONField(blank=True, null=True)

    eoi_a_is_eoi_return = models.TextField(blank=True, null=True)
    eoi_a_eoi_items = models.TextField(blank=True, null=True)
    service_charge = models.TextField(blank=True, null=True)
    assignment = models.TextField(blank=True, null=True)

    def save_image_from_url(self, url, image_field, save=True):
        say_my_name()
        # print('Download photo:', url)
        path = urlparse(url).path
        ext = os.path.splitext(path)[1]
        img_temp = NamedTemporaryFile(delete=True)
        try:
            context = urlopen(url, timeout=1)
            if context.getcode() == 200:
                img_temp.write(context.read())
                img_temp.flush()
                img_filename = f"image_{self.complex_id}" + ext
                image_field.save(img_filename, File(img_temp), save=save)
                # print('Ready')
            else:
                raise URLError
        except URLError as e:
            print('Error download photo:', str(e))
        except ValueError as e:
            print('Error download photo:', str(e))

    def save_listing_photos(self):
        say_my_name()
        if self.photo and not self.photo_main:
            self.save_image_from_url(self.photo, self.photo_main, save=False)

        photo_urls = json.loads(self.listing_album)
        # print(photo_urls)
        if len(photo_urls) >= 1:
            if not self.photo_1:
                self.save_image_from_url(photo_urls[0], self.photo_1, save=False)
        if len(photo_urls) >= 2:
            if not self.photo_2:
                self.save_image_from_url(photo_urls[1], self.photo_2, save=False)
        if len(photo_urls) >= 3:
            if not self.photo_3:
                self.save_image_from_url(photo_urls[2], self.photo_3, save=False)
        if len(photo_urls) >= 4:
            if not self.photo_4:
                self.save_image_from_url(photo_urls[3], self.photo_4, save=False)

    def save_main_album_images(self):
        say_my_name()
        # delete old, if exist
        self.mainalbumimage_set.all().delete()

        if self.listing_album is not None:
            photo_urls = json.loads(self.listing_album)
            for photo_url in photo_urls:
                new_image = self.mainalbumimage_set.create(photo=None)
                new_image.save()
                self.save_image_from_url(photo_url, new_image.photo)

    def save_prices(self):
        say_my_name()
        # delete old, if exist
        self.price_set.all().delete()

        if self.listing_br_prices is not None:
            prices = json.loads(self.listing_br_prices)
            for price in prices:
                price['min_area_m2'] = price['min_area']['m2']
                price['min_area_ft2'] = price['min_area']['ft2']
                price['max_area_m2'] = price['max_area']['m2']
                price['max_area_ft2'] = price['max_area']['ft2']
                price.pop('min_area', None)
                price.pop('max_area', None)
                self.price_set.create(**price)

    def save_amenities(self):
        say_my_name()
        # delete old, if exist
        self.amenity_set.all().delete()

        if self.listing_amenities is not None:
            amenities = json.loads(self.listing_amenities)
            for amenity in amenities:
                self.amenity_set.create(**amenity)

    def save_districts(self):
        say_my_name()
        # delete old, if exist
        self.district_set.all().delete()

        if self.listing_districts is not None:
            districts = json.loads(self.listing_districts)
            for district in districts:
                self.district_set.create(name=district)

    def save_albums(self):
        say_my_name()
        # delete old, if exist
        self.album_set.all().delete()

        if self.listing_albums is not None:
            albums = json.loads(self.listing_albums)
            for album in albums:
                album['title_ru'] = album['title']['ru']
                album['title_en'] = album['title']['en']
                album['title_ar'] = album['title']['ar']
                album.pop('title', None)
                images = album.pop('images', None)
                new_album = self.album_set.create(**album)
                for image_url in images['image']:
                    new_image = new_album.image_set.create(photo=None)  # self.save_image_from_url(image)
                    self.save_image_from_url(image_url, new_image.photo)

    def save_payment_plans(self):
        say_my_name()
        # delete old, if exist
        self.paymentplan_set.all().delete()

        if self.listing_payment_plans is not None:
            payment_plans = json.loads(self.listing_payment_plans)
            # print(payment_plans)
            for payment_plan in payment_plans:
                payment_plan['title_ru'] = payment_plan['title']['ru']
                payment_plan['title_en'] = payment_plan['title']['en']
                payment_plan['title_ar'] = payment_plan['title']['ar']
                payment_plan.pop('title', None)
                additions = payment_plan.pop('additional', None)
                if not isinstance(additions, list):
                    additions = [additions, ]
                payment_plan['period_after_handover_period'] = payment_plan['period_after_handover']['period']
                payment_plan['period_after_handover_count'] = payment_plan['period_after_handover']['count']
                payment_plan['period_after_handover_repeat_count'] = payment_plan['period_after_handover'][
                    'repeat_count']
                payment_plan.pop('period_after_handover', None)
                payment_plan['period_after_roi_period'] = payment_plan['period_after_roi']['period']
                payment_plan['period_after_roi_count'] = payment_plan['period_after_roi']['count']
                payment_plan['period_after_roi_repeat_count'] = payment_plan['period_after_roi']['repeat_count']
                payment_plan.pop('period_after_roi', None)
                new_payment_plan = self.paymentplan_set.create(**payment_plan)
                for additional in additions:
                    if additional:
                        additional['title_ru'] = additional['title']['ru']
                        additional['title_en'] = additional['title']['en']
                        additional['title_ar'] = additional['title']['ar']
                        additional.pop('title', None)
                        new_payment_plan.additional_set.create(**additional)

    def save(self, **kwargs):
        say_my_name()
        if self.is_fully_loaded:
            print(f'save is_fully_loaded for complex-id = {self.complex_id}')
            super().save(**kwargs)  # Call the "real" save() method.
        else:
            print(f'save listing for complex-id = {self.complex_id}')
            self.save_listing_photos()
            super().save(**kwargs)  # Call the "real" save() method.
            # do_something()
            self.save_main_album_images()
            self.save_prices()
            self.save_amenities()
            self.save_districts()
            self.save_albums()
            self.save_payment_plans()
            # do_something_else()
            self.is_fully_loaded = True
            self.save(update_fields=['is_fully_loaded'])

    def __str__(self):
        if self.title_a_en is None:
            if self.title_a_ru is None:
                if self.title_a_ar is None:
                    return "NO TITLE OFFER"
                else:
                    return self.title_a_ar
            else:
                return self.title_a_ru
        else:
            return self.title_a_en


class MainAlbumImage(models.Model):
    album = models.ForeignKey(Listing, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.photo.url


class Price(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    # "[{\"key\": \"rooms_2\", \"count\": \"1\", \"min_price\": \"2300888\", \"max_price\": \"2300888\", \"min_price_m2\": \"22152\", \"max_price_m2\": \"22152\", \"currency\": \"AED\", \"min_area\": {\"m2\": \"103.87\", \"ft2\": \"1118.05\"}, \"max_area\": {\"m2\": \"103.87\", \"ft2\": \"1118.05\"}}, {\"key\": \"rooms_3\", \"count\": \"5\", \"min_price\": \"4662888\", \"max_price\": \"4687888\", \"min_price_m2\": \"18205\", \"max_price_m2\": \"18229\", \"currency\": \"AED\", \"min_area\": {\"m2\": \"256.04\", \"ft2\": \"2755.99\"}, \"max_area\": {\"m2\": \"257.25\", \"ft2\": \"2769.01\"}}]"
    key = models.TextField(blank=True, null=True)
    count = models.IntegerField(null=True)
    min_price = models.FloatField(null=True)
    max_price = models.FloatField(null=True)
    min_price_m2 = models.FloatField(null=True)
    max_price_m2 = models.FloatField(null=True)
    currency = models.TextField(blank=True, null=True)
    min_area_m2 = models.FloatField(null=True)
    max_area_m2 = models.FloatField(null=True)
    min_area_ft2 = models.FloatField(null=True)
    max_area_ft2 = models.FloatField(null=True)

    def __str__(self):
        return f'{self.key} price from {self.min_price} to {self.max_price} {self.currency}'


class Amenity(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    ru = models.TextField(blank=True, null=True)
    en = models.TextField(blank=True, null=True)
    ar = models.TextField(blank=True, null=True)
    amenity_svg = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.en


class District(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    title_ru = models.TextField(blank=True, null=True)
    title_en = models.TextField(blank=True, null=True)
    title_ar = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_en


class Image(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.photo.url


class PaymentPlan(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    title_ru = models.TextField(blank=True, null=True)
    title_en = models.TextField(blank=True, null=True)
    title_ar = models.TextField(blank=True, null=True)
    on_booking_percent = models.FloatField(null=True)
    on_booking_fix = models.FloatField(blank=True, null=True)
    on_construction_percent = models.FloatField(null=True)
    on_construction_fix = models.FloatField(blank=True, null=True)
    on_construction_payments_count = models.IntegerField(null=True)
    on_handover_percent = models.FloatField(blank=True, null=True)
    on_handover_fix = models.FloatField(blank=True, null=True)
    on_handover_payments_count = models.IntegerField(null=True)
    post_handover_percent = models.FloatField(blank=True, null=True)
    post_handover_fix = models.FloatField(blank=True, null=True)
    on_post_handover_payments_count = models.IntegerField(null=True)
    additional_percent = models.FloatField(null=True)
    additional_fix = models.FloatField(null=True)
    roi_percent = models.FloatField(blank=True, null=True)
    roi_fix = models.FloatField(blank=True, null=True)
    roi_payments_count = models.IntegerField(null=True)
    currency = models.TextField(blank=True, null=True)
    period_after_handover_period = models.TextField(blank=True, null=True)
    period_after_handover_count = models.TextField(blank=True, null=True)
    period_after_handover_repeat_count = models.TextField(blank=True, null=True)
    period_after_roi_period = models.TextField(blank=True, null=True)
    period_after_roi_count = models.TextField(blank=True, null=True)
    period_after_roi_repeat_count = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title_en


class Additional(models.Model):
    payment_plan = models.ForeignKey(PaymentPlan, on_delete=models.CASCADE)
    title_ru = models.TextField(blank=True, null=True)
    title_en = models.TextField(blank=True, null=True)
    title_ar = models.TextField(blank=True, null=True)
    percent = models.FloatField(null=True)
    fix = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title_en
