# Generated by Django 5.0.1 on 2024-02-06 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_en', models.CharField(max_length=200)),
                ('title_ru', models.CharField(max_length=200)),
                ('title_ar', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('pdf', models.FileField(upload_to='pdf/%Y/%m/%d/')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
