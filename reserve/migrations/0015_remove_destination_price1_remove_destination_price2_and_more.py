# Generated by Django 4.2.2 on 2023-07-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0014_remove_zone_barrio_zone_barrios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='price2',
        ),
        migrations.AddField(
            model_name='destination',
            name='zone',
            field=models.ManyToManyField(to='reserve.zone', verbose_name='Zona'),
        ),
    ]
