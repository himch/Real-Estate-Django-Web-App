# Generated by Django 3.1.1 on 2024-01-19 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_contact_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='feedback_method',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
