# Generated by Django 3.1.1 on 2024-01-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20240118_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='page',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
