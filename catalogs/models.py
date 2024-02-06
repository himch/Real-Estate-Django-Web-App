from django.db import models


# Create your models here.


class Catalog(models.Model):
	title_en = models.CharField(max_length=200)
	title_ru = models.CharField(max_length=200)
	title_ar = models.CharField(max_length=200)
	description_en = models.CharField(max_length=500)
	description_ru = models.CharField(max_length=500)
	description_ar = models.CharField(max_length=500)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	pdf_en = models.FileField(upload_to="pdf/%Y/%m/%d/")
	pdf_ru = models.FileField(upload_to="pdf/%Y/%m/%d/")
	pdf_ar = models.FileField(upload_to="pdf/%Y/%m/%d/")
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title_en
