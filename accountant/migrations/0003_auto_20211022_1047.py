# Generated by Django 3.2.7 on 2021-10-22 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0002_alter_accountant_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountant',
            name='balace',
        ),
        migrations.AddField(
            model_name='accountant',
            name='balance_due',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 22, 10, 47, 36, 690804)),
        ),
    ]
