# Generated by Django 5.0.1 on 2024-02-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0001_initial'),
        ('listings', '0032_alter_additional_payment_plan_alter_album_listing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='listings',
            field=models.ManyToManyField(related_name='developers', to='listings.listing'),
        ),
    ]
