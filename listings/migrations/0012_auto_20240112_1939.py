# Generated by Django 3.1.1 on 2024-01-12 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20240112_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_amenities',
            field=models.TextField(blank=True, null=True),
        ),
    ]
