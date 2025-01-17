# Generated by Django 5.0.1 on 2024-02-26 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0009_remove_profile_avatar_remove_profile_bio'),
        ('listings', '0033_listing_developer_alter_listing_realtor'),
        ('realtors', '0004_alter_realtor_experience_ar_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_category', models.CharField(choices=[('LONG-TERM', 'Long-Term'), ('MID-TERM', 'Mid-Term'), ('SHORT-TERM', 'Short-Term')], default='MID-TERM', max_length=12)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('price_per_month', models.IntegerField(blank=True, null=True)),
                ('total_months', models.IntegerField(blank=True, null=True)),
                ('price_per_day', models.IntegerField(blank=True, null=True)),
                ('total_days', models.IntegerField(blank=True, null=True)),
                ('numbers_of_cleanings', models.IntegerField(blank=True, null=True)),
                ('cleaning_cost', models.IntegerField(blank=True, null=True)),
                ('numbers_of_concierge_services', models.IntegerField(blank=True, null=True)),
                ('concierge_service_cost', models.IntegerField(blank=True, null=True)),
                ('info', models.CharField(max_length=255, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.profile')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservations',
                'db_table': 'reservations',
                'ordering': ['-id'],
            },
        ),
    ]
