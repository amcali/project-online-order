# Generated by Django 2.2.7 on 2019-11-20 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_remove_charge_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charge',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='charge',
            name='street_address1',
        ),
        migrations.RemoveField(
            model_name='charge',
            name='street_address2',
        ),
        migrations.RemoveField(
            model_name='charge',
            name='town_or_city',
        ),
    ]
