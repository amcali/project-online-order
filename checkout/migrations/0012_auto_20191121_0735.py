# Generated by Django 2.2.7 on 2019-11-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_auto_20191121_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitem',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='lineitem',
            name='name',
        ),
        migrations.RemoveField(
            model_name='lineitem',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='lineitem',
            name='transaction',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
