from django.db import models
from datetime import datetime
from tinymce.models import HTMLField


class Realtor(models.Model):
    name_en = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    name_ru = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    job_title_en = models.CharField(max_length=200)
    job_title_ru = models.CharField(max_length=200)
    job_title_ar = models.CharField(max_length=200)
    experience_en = models.CharField(max_length=200)
    experience_ru = models.CharField(max_length=200)
    experience_ar = models.CharField(max_length=200)
    specialization_en = models.CharField(max_length=200)
    specialization_ru = models.CharField(max_length=200)
    specialization_ar = models.CharField(max_length=200)
    language_en = models.CharField(max_length=200)
    language_ru = models.CharField(max_length=200)
    language_ar = models.CharField(max_length=200)
    description_en = HTMLField()
    description_ru = HTMLField()
    description_ar = HTMLField()

    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    whatsapp = models.CharField(blank=True, null=True, max_length=100)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name_en
