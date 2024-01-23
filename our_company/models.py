from django.db import models


class OurCompany(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200)
    office_address = models.CharField(blank=True, null=True, max_length=200)
    office_coordinates_longitude = models.CharField(blank=True, null=True, max_length=100)
    office_coordinates_latitude = models.CharField(blank=True, null=True, max_length=100)
    office_timezone = models.CharField(blank=True, null=True, max_length=100)
    office_working_hours = models.CharField(blank=True, null=True, max_length=100)
    email = models.CharField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)
    whatsapp = models.CharField(blank=True, null=True, max_length=100)
    telegram = models.CharField(blank=True, null=True, max_length=100)
    instagram = models.CharField(blank=True, null=True, max_length=100)
    youtube = models.CharField(blank=True, null=True, max_length=100)
    vk = models.CharField(blank=True, null=True, max_length=100)
    dzen = models.CharField(blank=True, null=True, max_length=100)
    facebook = models.CharField(blank=True, null=True, max_length=100)
    linkedin = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.name
