# Generated by Django 4.2.2 on 2023-07-15 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0015_remove_destination_price1_remove_destination_price2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='barrios',
        ),
    ]
