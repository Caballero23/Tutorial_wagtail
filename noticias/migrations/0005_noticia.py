# Generated by Django 3.2.11 on 2022-02-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_noticiaspage_portada'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='título')),
                ('link', models.URLField()),
                ('date', models.DateField()),
                ('imagen', models.URLField()),
            ],
        ),
    ]