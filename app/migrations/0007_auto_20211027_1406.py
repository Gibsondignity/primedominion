# Generated by Django 3.2.8 on 2021-10-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_contract_account_officer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='due_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='start_date',
            field=models.DateField(),
        ),
    ]
