# Generated by Django 5.0.1 on 2024-02-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_chapter_ar_alter_article_chapter_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='chapter_ar',
            field=models.CharField(max_length=50, verbose_name='Chapter ar'),
        ),
        migrations.AlterField(
            model_name='article',
            name='chapter_en',
            field=models.CharField(max_length=50, verbose_name='Chapter en'),
        ),
        migrations.AlterField(
            model_name='article',
            name='chapter_ru',
            field=models.CharField(max_length=50, verbose_name='Chapter ru'),
        ),
    ]
