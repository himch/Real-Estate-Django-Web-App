# Generated by Django 5.0.1 on 2024-03-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_company', '0003_auto_20240122_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourcompany',
            name='rent_cleaning_cost_usd',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ourcompany',
            name='rent_concierge_service_usd',
            field=models.IntegerField(null=True),
        ),
    ]
