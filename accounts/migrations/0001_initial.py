# Generated by Django 5.0.1 on 2024-02-14 18:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('avatar', models.ImageField(blank=True, default='img/default_avatar.webp', upload_to='images/avatars/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], verbose_name='Avatar')),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='Bio')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'app_profiles',
                'ordering': ('user',),
            },
        ),
    ]
