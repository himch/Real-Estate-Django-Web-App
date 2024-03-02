import json
import os
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import URLError

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from datetime import datetime
from django_admin_geomap import GeoItem

from developers.models import Developer
from listings.utils import fix_description, json_equal
from modules.services.utils import say_my_name
from realtors.models import Realtor

User = get_user_model()

RENT_OFFER_TYPE = "rent"
SELL_OFFER_TYPE = "sell"

OFFER_TYPE_CHOICES = (
    (RENT_OFFER_TYPE, "Rent"),
    (SELL_OFFER_TYPE, "Sell"),
)

SUITABLE_FOR_1 = "1 guest"
SUITABLE_FOR_2 = "2 guests"
SUITABLE_FOR_3 = "3 guests"
SUITABLE_FOR_4 = "More than 3 guests"

SUITABLE_FOR_CHOICES = (
    (1, SUITABLE_FOR_1),
    (2, SUITABLE_FOR_2),
    (3, SUITABLE_FOR_3),
    (4, SUITABLE_FOR_4),
)


class DisplayedSellListingManager(models.Manager):
    def get_queryset(self):
        return super(DisplayedSellListingManager, self).get_queryset().filter(is_published=True,
                                                                              is_fully_loaded=True,
                                                                              offer_type=SELL_OFFER_TYPE).order_by('-list_date')


class DisplayedRentListingManager(models.Manager):
    def get_queryset(self):
        return super(DisplayedRentListingManager, self).get_queryset().filter(is_published=True,
                                                                              is_fully_loaded=True,
                                                                              offer_type=RENT_OFFER_TYPE).order_by('-list_date')


class Listing(models.Model, GeoItem):
    objects = models.Manager()
    sell_objects = DisplayedSellListingManager()
    rent_objects = DisplayedRentListingManager()

    source = models.CharField(max_length=10, default='alnair')
    offer_type = models.CharField(max_length=4, choices=OFFER_TYPE_CHOICES, default=SELL_OFFER_TYPE)
    url = models.URLField(blank=True, null=True)
    realtor = models.ForeignKey(Realtor, blank=True, null=True, on_delete=models.DO_NOTHING)
    developer = models.ForeignKey(Developer, on_delete=models.DO_NOTHING)

    address = models.CharField(max_length=200)

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_main_thumbnail_281_417 = ImageSpecField(source='photo_main',
                                                  processors=[ResizeToFill(width=281, height=417, upscale=False)],
                                                  format='WEBP',
                                                  options={'quality': 100})
    photo_main_thumbnail_width_180 = ImageSpecField(source='photo_main',
                                                    processors=[ResizeToFill(width=180, height=180, upscale=False)],
                                                    format='WEBP',
                                                    options={'quality': 100})
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    suitable_for = models.IntegerField(choices=SUITABLE_FOR_CHOICES, default=4)  # for RENT

    @property
    def suitable_for_string(self):
        for number, item in SUITABLE_FOR_CHOICES:
            if number == self.suitable_for:
                return item
        number, item = SUITABLE_FOR_CHOICES[0]
        return item

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True, blank=True)

    def _get_planned_completion(self):
        if self.planned_completion_at:
            return self.planned_completion_at[:7]
        else:
            return None

    planned_completion = property(_get_planned_completion)

    complex_id = models.IntegerField(null=True, unique=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    photo = models.URLField(blank=True, null=True)

    title_a_ru = models.CharField(max_length=200, blank=True, null=True)
    title_a_en = models.CharField(max_length=200, blank=True, null=True)
    title_a_ar = models.CharField(max_length=200, blank=True, null=True)

    description_a_ru = models.TextField(blank=True, null=True)
    description_a_en = models.TextField(blank=True, null=True)
    description_a_ar = models.TextField(blank=True, null=True)

    special_price = models.IntegerField(blank=True, null=True, default=0)

    price_on_request = models.IntegerField(blank=True, null=True)
    is_limited_publication = models.IntegerField(blank=True, null=True)

    status_a_ru = models.CharField(max_length=200, blank=True, null=True)
    status_a_en = models.CharField(max_length=200, blank=True, null=True)
    status_a_ar = models.CharField(max_length=200, blank=True, null=True)

    construction_start_at = models.CharField(max_length=200, blank=True, null=True)
    construction_progress = models.FloatField(null=True)
    planned_completion_at = models.CharField(max_length=200, blank=True, null=True)
    predicted_completion_at = models.CharField(max_length=200, blank=True, null=True)

    developer_a_title_a_ru = models.CharField(max_length=200, blank=True, null=True)
    developer_a_title_a_en = models.CharField(max_length=200, blank=True, null=True)
    developer_a_title_a_ar = models.CharField(max_length=200, blank=True, null=True)
    developer_a_logo = models.CharField(max_length=200, blank=True, null=True)

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
    price_a_currency = models.CharField(max_length=200, blank=True, null=True)

    listing_br_prices = models.JSONField(blank=True, null=True)

    updated_at = models.CharField(max_length=200, blank=True, null=True)

    is_sold_out = models.IntegerField(null=True)
    listing_payment_plans = models.JSONField(blank=True, null=True)

    sales_status_a_ru = models.CharField(max_length=200, blank=True, null=True)
    sales_status_a_en = models.CharField(max_length=200, blank=True, null=True)
    sales_status_a_ar = models.CharField(max_length=200, blank=True, null=True)

    listing_stocks = models.JSONField(blank=True, null=True)

    eoi_a_is_eoi_return = models.CharField(max_length=200, blank=True, null=True)
    eoi_a_eoi_items = models.TextField(blank=True, null=True)
    service_charge = models.CharField(max_length=200, blank=True, null=True)
    assignment = models.CharField(max_length=200, blank=True, null=True)

    @classmethod
    def from_db(cls, db, field_names, values):
        say_my_name()
        instance = super().from_db(db, field_names, values)

        # save original values, when model is loaded from database,
        # in a separate attribute on the model
        instance._loaded_values = dict(zip(field_names, values))
        # print('old Listing values saves')
        return instance

    def save_image_from_url(self, url, image_field, save=True):
        say_my_name()
        # print('Download photo:', url)
        path = urlparse(url).path
        ext = os.path.splitext(path)[1]
        img_temp = NamedTemporaryFile(delete=True)
        try:
            context = urlopen(url, timeout=10)
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
        except TimeoutError as e:
            print('Error download photo:', str(e))

    def save_listing_photos(self):
        say_my_name()
        if self.photo and not self.photo_main:
            self.save_image_from_url(self.photo, self.photo_main, save=False)

        if self._my_updating and self._loaded_values['photo'] != self.photo:
            self.save_image_from_url(self.photo, self.photo_main, save=False)

        if self.listing_album is not None:
            if (self._my_adding or
                    (self._my_updating and not json_equal(self._loaded_values['listing_album'],
                                                          self.listing_album))):
                try:
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
                except json.decoder.JSONDecodeError:
                    print('Error - json.loads, try to read as string and save listing_photo 1')
                    if not self.photo_1:
                        self.save_image_from_url(self.listing_album, self.photo_1, save=False)

    def save_main_album_images(self):
        say_my_name()
        if (self._my_adding or
                (self._my_updating and not json_equal(self._loaded_values['listing_album'],
                                                      self.listing_album))):
            # delete old, if exist
            for obj in self.main_album_images.all():
                obj.delete()

            if self.listing_album is not None:
                try:
                    photo_urls = json.loads(self.listing_album)
                    for photo_url in photo_urls:
                        new_image = self.main_album_images.create(photo=None)
                        new_image.save()
                        self.save_image_from_url(photo_url, new_image.photo)
                except json.decoder.JSONDecodeError:
                    print('Error - json.loads, try to read as string and save main_album_images')
                    new_image = self.main_album_images.create(photo=None)
                    new_image.save()
                    self.save_image_from_url(self.listing_album, new_image.photo)

    def save_prices(self):
        say_my_name()
        if (self._my_adding or
                (self._my_updating and not json_equal(self._loaded_values['listing_br_prices'],
                                                      self.listing_br_prices))):
            # delete old, if exist
            for obj in self.prices.all():
                obj.delete()

            if self.listing_br_prices is not None:
                try:
                    prices = json.loads(self.listing_br_prices)
                    for price in prices:
                        price['min_area_m2'] = price['min_area']['m2']
                        price['min_area_ft2'] = price['min_area']['ft2']
                        price['max_area_m2'] = price['max_area']['m2']
                        price['max_area_ft2'] = price['max_area']['ft2']
                        price.pop('min_area', None)
                        price.pop('max_area', None)
                        self.prices.create(**price)
                except json.decoder.JSONDecodeError:
                    print('Error - json.loads. Cant create prices')

    def save_amenities(self):
        say_my_name()
        if (self._my_adding or
                (self._my_updating and not json_equal(self._loaded_values['listing_amenities'],
                                                      self.listing_amenities))):
            # delete old, if exist
            for obj in self.amenities.all():
                obj.delete()

            if self.listing_amenities is not None:
                try:
                    amenities = json.loads(self.listing_amenities)
                    for amenity in amenities:
                        self.amenities.create(**amenity)
                except json.decoder.JSONDecodeError:
                    print('Error - json.loads. Cant create amenities')

    def save_districts(self):
        say_my_name()
        if (self._my_adding or
                (self._my_updating and not json_equal(self._loaded_values['listing_districts'],
                                                      self.listing_districts))):
            # delete old, if exist
            for obj in self.districts.all():
                obj.delete()

            if self.listing_districts is not None:
                try:
                    districts = json.loads(self.listing_districts)
                    for district in districts:
                        self.districts.create(name=district)
                except json.decoder.JSONDecodeError:
                    print('Error - json.loads. Cant create districts. Try to load one')
                    self.districts.create(name=self.listing_districts)

    def save_albums(self):
        say_my_name()
        if (self._my_adding or
                (self._my_updating and not json_equal(self._loaded_values['listing_albums'],
                                                      self.listing_albums))):
            # delete old, if exist
            for album in self.albums.all():
                for obj in album.images.all():
                    obj.delete()
                album.delete()

            if self.listing_albums is not None:
                try:
                    albums = json.loads(self.listing_albums)
                    for album in albums:
                        album['title_ru'] = album['title']['ru']
                        album['title_en'] = album['title']['en']
                        album['title_ar'] = album['title']['ar']
                        album.pop('title', None)
                        images = album.pop('images', None)
                        new_album = self.albums.create(**album)
                        if isinstance(images['image'], str):
                            new_image = new_album.images.create(photo=None)  # self.save_image_from_url(image)
                            self.save_image_from_url(images['image'], new_image.photo)
                        else:
                            for image_url in images['image']:
                                new_image = new_album.images.create(photo=None)  # self.save_image_from_url(image)
                                self.save_image_from_url(image_url, new_image.photo)
                except json.decoder.JSONDecodeError:
                    print('Error - json.loads. Cant create albums')

    def save_payment_plans(self):
        say_my_name()
        if (self._my_adding or
                (self._my_updating and not json_equal(self._loaded_values['listing_payment_plans'],
                                                      self.listing_payment_plans))):
            # delete old, if exist
            for payment_plan in self.payment_plans.all():
                for obj in payment_plan.additionals.all():
                    obj.delete()
                payment_plan.delete()

            if self.listing_payment_plans is not None:
                try:
                    payment_plans = json.loads(self.listing_payment_plans)
                    # print(payment_plans)
                    for payment_plan in payment_plans:
                        payment_plan['alnair_id'] = payment_plan['id']
                        payment_plan.pop('id', None)
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
                        new_payment_plan = self.payment_plans.create(**payment_plan)
                        for additional in additions:
                            if additional:
                                additional['title_ru'] = additional['title']['ru']
                                additional['title_en'] = additional['title']['en']
                                additional['title_ar'] = additional['title']['ar']
                                additional.pop('title', None)
                                new_payment_plan.additionals.create(**additional)
                except json.decoder.JSONDecodeError:
                    print('Error - json.loads. Cant create payment_plan')

    def save(self, **kwargs):
        say_my_name()
        # print('save Listing...')
        self._my_updating = self._state.adding is False  # эта запись обновляется, а не добавляется
        self._my_adding = self._state.adding is True  # эта запись обновляется, а не добавляется
        self.description_a_en = fix_description(self.description_a_en)
        self.description_a_ru = fix_description(self.description_a_ru)
        self.description_a_ar = fix_description(self.description_a_ar)
        if self.is_fully_loaded:
            # print(f'save is_fully_loaded for complex-id = {self.complex_id}')
            super().save(**kwargs)  # Call the "real" save() method.
        else:
            # print(f'save listing for complex-id = {self.complex_id}')
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
    album = models.ForeignKey(Listing, related_name='main_album_images', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.photo.url


class Price(models.Model):
    listing = models.ForeignKey(Listing, related_name='prices', on_delete=models.CASCADE)
    # "[{\"key\": \"rooms_2\", \"count\": \"1\", \"min_price\": \"2300888\", \"max_price\": \"2300888\", \"min_price_m2\": \"22152\", \"max_price_m2\": \"22152\", \"currency\": \"AED\", \"min_area\": {\"m2\": \"103.87\", \"ft2\": \"1118.05\"}, \"max_area\": {\"m2\": \"103.87\", \"ft2\": \"1118.05\"}}, {\"key\": \"rooms_3\", \"count\": \"5\", \"min_price\": \"4662888\", \"max_price\": \"4687888\", \"min_price_m2\": \"18205\", \"max_price_m2\": \"18229\", \"currency\": \"AED\", \"min_area\": {\"m2\": \"256.04\", \"ft2\": \"2755.99\"}, \"max_area\": {\"m2\": \"257.25\", \"ft2\": \"2769.01\"}}]"
    key = models.CharField(max_length=200, blank=True, null=True)
    count = models.IntegerField(null=True)
    min_price = models.FloatField(null=True)
    max_price = models.FloatField(null=True)
    min_price_m2 = models.FloatField(null=True)
    max_price_m2 = models.FloatField(null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    min_area_m2 = models.FloatField(null=True)
    max_area_m2 = models.FloatField(null=True)
    min_area_ft2 = models.FloatField(null=True)
    max_area_ft2 = models.FloatField(null=True)

    def __str__(self):
        return f'{self.key} price from {self.min_price} to {self.max_price} {self.currency}'


class Amenity(models.Model):
    listing = models.ForeignKey(Listing, related_name='amenities', on_delete=models.CASCADE)
    ru = models.CharField(max_length=200, blank=True, null=True)
    en = models.CharField(max_length=200, blank=True, null=True)
    ar = models.CharField(max_length=200, blank=True, null=True)
    amenity_svg = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.en


class District(models.Model):
    listing = models.ForeignKey(Listing, related_name='districts', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    listing = models.ForeignKey(Listing, related_name='albums', on_delete=models.CASCADE)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ar = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title_en


class Image(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.photo.url


class PaymentPlan(models.Model):
    listing = models.ForeignKey(Listing, related_name='payment_plans', on_delete=models.CASCADE)
    alnair_id = models.IntegerField(null=True)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ar = models.CharField(max_length=200, blank=True, null=True)
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
    currency = models.CharField(max_length=20, blank=True, null=True)
    period_after_handover_period = models.CharField(max_length=200, blank=True, null=True)
    period_after_handover_count = models.CharField(max_length=200, blank=True, null=True)
    period_after_handover_repeat_count = models.CharField(max_length=200, blank=True, null=True)
    period_after_roi_period = models.CharField(max_length=200, blank=True, null=True)
    period_after_roi_count = models.CharField(max_length=200, blank=True, null=True)
    period_after_roi_repeat_count = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title_en


class Additional(models.Model):
    payment_plan = models.ForeignKey(PaymentPlan, related_name='additionals', on_delete=models.CASCADE)
    title_ru = models.CharField(max_length=200, blank=True, null=True)
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_ar = models.CharField(max_length=200, blank=True, null=True)
    percent = models.FloatField(null=True)
    fix = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.title_en


class Bookmark(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, verbose_name="Listing", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'
        ordering = ['-id']
        db_table = "bookmark_listing"

    def __str__(self):
        return self.user.username


class Favorite(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, verbose_name="Listing", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        ordering = ['-id']
        db_table = "favorite_listing"

    def __str__(self):
        return self.user.username
