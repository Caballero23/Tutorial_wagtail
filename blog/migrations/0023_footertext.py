# Generated by Django 3.2.11 on 2022-03-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_deportepage_peliculapage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Footer',
            },
        ),
    ]