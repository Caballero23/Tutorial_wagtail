# Generated by Django 3.2.11 on 2022-03-08 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('blog', '0023_footertext'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MusicaPage',
        ),
    ]
