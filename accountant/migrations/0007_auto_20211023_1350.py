# Generated by Django 3.2.7 on 2021-10-23 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0006_auto_20211023_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountant',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='accountant',
            name='balance_due',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 23, 13, 50, 42, 238184)),
        ),
    ]
