# Generated by Django 2.2.7 on 2019-11-20 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='quantity',
        ),
    ]
