# Generated by Django 5.0.1 on 2024-01-31 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0029_listing_key_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='key_mode',
        ),
    ]
