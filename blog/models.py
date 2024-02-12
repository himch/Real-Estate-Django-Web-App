from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from tinymce.models import HTMLField

User = get_user_model()


class Article(models.Model):
    """
    Модель постов для сайта
    """
    STATUS_OPTIONS = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )

    title_en = models.CharField(verbose_name='Title en', max_length=255)
    title_ru = models.CharField(verbose_name='Title ru', max_length=255)
    title_ar = models.CharField(verbose_name='Title ar', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True, unique=True)
    category_en = models.CharField(verbose_name='Chapter en', max_length=50)
    category_ru = models.CharField(verbose_name='Chapter ru', max_length=50)
    category_ar = models.CharField(verbose_name='Chapter ar', max_length=50)
    text_en = HTMLField()
    text_ru = HTMLField()
    text_ar = HTMLField()
    # text_en = models.TextField(verbose_name='Text en')
    # text_ru = models.TextField(verbose_name='Text ru')
    # text_ar = models.TextField(verbose_name='Text ar')
    photo = models.ImageField(
        verbose_name='Post preview photo',
        blank=True,
        upload_to='photos/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Post status', max_length=10)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Create time')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Update time')
    author = models.ForeignKey(to=User, verbose_name='Author', on_delete=models.SET_DEFAULT, related_name='author_posts', default=1)
    updater = models.ForeignKey(to=User, verbose_name='Updater', on_delete=models.SET_NULL, null=True, related_name='updater_posts', blank=True)
    fixed = models.BooleanField(verbose_name='Fixed', default=False)

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title_en)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'app_articles'
        ordering = ['-fixed', '-time_create']
        indexes = [models.Index(fields=['-fixed', '-time_create', 'status'])]
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title_en
