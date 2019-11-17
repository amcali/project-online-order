# Generated by Django 2.2.7 on 2019-11-17 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20191116_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('uncollected', 'Uncollected'), ('collected', 'Collected')], max_length=50)),
                ('charge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkout.Charge')),
            ],
        ),
    ]
