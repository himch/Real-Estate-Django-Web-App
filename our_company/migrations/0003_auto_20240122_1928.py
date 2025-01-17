# Generated by Django 3.1.1 on 2024-01-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_company', '0002_auto_20240122_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourcompany',
            old_name='address',
            new_name='office_address',
        ),
        migrations.AddField(
            model_name='ourcompany',
            name='office_coordinates_latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourcompany',
            name='office_coordinates_longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourcompany',
            name='office_timezone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourcompany',
            name='office_working_hours',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
