# Generated by Django 3.1.1 on 2024-01-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourcompany',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ourcompany',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
