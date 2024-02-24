# Generated by Django 5.0.1 on 2024-02-24 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0007_alter_developer_text_ar_alter_developer_text_en_and_more'),
        ('listings', '0032_alter_additional_payment_plan_alter_album_listing_and_more'),
        ('realtors', '0004_alter_realtor_experience_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='developer',
            field=models.ForeignKey(default=55, on_delete=django.db.models.deletion.DO_NOTHING, to='developers.developer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]
