# Generated by Django 3.2.8 on 2021-10-27 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountant',
            old_name='swift_code',
            new_name='invoice_number',
        ),
    ]
