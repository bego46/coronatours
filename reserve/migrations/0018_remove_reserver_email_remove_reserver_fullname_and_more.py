# Generated by Django 4.2.2 on 2023-07-15 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0017_remove_destination_zone_destination_barrio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserver',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reserver',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='reserver',
            name='phone',
        ),
    ]
