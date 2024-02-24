# Generated by Django 5.0.1 on 2024-02-24 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developers', '0004_alter_developer_developer_a_logo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='developer_a_logo',
            new_name='logo',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='developer_a_title_a_ar',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='developer_a_title_a_en',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='developer_a_title_a_ru',
        ),
        migrations.RemoveField(
            model_name='developer',
            name='listings',
        ),
        migrations.AddField(
            model_name='developer',
            name='title_ar',
            field=models.CharField(default='NONE', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='developer',
            name='title_en',
            field=models.CharField(default='NONE', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='developer',
            name='title_ru',
            field=models.CharField(default='NONE', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='developer',
            name='main_office',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
