from django.contrib import admin
from .models import Article

admin.site.register(Article)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_en',)}