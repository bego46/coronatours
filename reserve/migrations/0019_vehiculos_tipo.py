# Generated by Django 4.2.2 on 2023-07-17 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0018_remove_reserver_email_remove_reserver_fullname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculos',
            name='tipo',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Tipo'),
            preserve_default=False,
        ),
    ]
