from django.db import models
from datetime import datetime
from django.utils import timezone


class Contact(models.Model):
    listing = models.CharField(blank=True, null=True, max_length=200)
    listing_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(blank=True, null=True, max_length=200)
    email = models.CharField(blank=True, null=True, max_length=100)
    phone = models.CharField(blank=True, null=True, max_length=100)
    message = models.TextField(blank=True, null=True)
    contact_date = models.DateTimeField(default=timezone.now, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    consent_processing_personal_data = models.IntegerField(null=True, blank=True)
    page = models.CharField(blank=True, null=True, max_length=100)
    feedback_method = models.CharField(blank=True, null=True, max_length=25)

    def __str__(self):
        return self.name
