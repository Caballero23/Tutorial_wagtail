# Generated by Django 3.2.11 on 2022-02-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('pelis', '0003_auto_20220201_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
            },
        ),
        migrations.AddField(
            model_name='pelicula',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.DeleteModel(
            name='PelisPage',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='generos',
            field=models.ManyToManyField(to='pelis.Genre'),
        ),
    ]
