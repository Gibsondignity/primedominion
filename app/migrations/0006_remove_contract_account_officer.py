# Generated by Django 3.2.8 on 2021-10-27 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_acuser_pauser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='account_officer',
        ),
    ]