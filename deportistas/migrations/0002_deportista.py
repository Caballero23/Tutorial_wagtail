# Generated by Django 3.2.11 on 2022-03-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deportistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='deportista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.CharField(max_length=250, verbose_name='año')),
                ('nombre', models.CharField(max_length=250, verbose_name='nombre')),
                ('deporte', models.CharField(max_length=250, verbose_name='deporte')),
            ],
        ),
    ]
