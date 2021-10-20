# Generated by Django 3.2.7 on 2021-10-19 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your full name', max_length=50)),
                ('contact', models.PositiveIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(help_text='Enter your email address', max_length=50)),
                ('bank_details', models.CharField(help_text='Summary of bank details', max_length=200, null=True)),
                ('Bank_name', models.CharField(max_length=50, null=True)),
                ('Bank_address', models.CharField(max_length=50, null=True)),
                ('Bank_account_name', models.CharField(max_length=50, null=True)),
                ('Bank_account_number', models.CharField(max_length=50, null=True)),
                ('swift_code', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=50, null=50)),
                ('start_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_name', models.CharField(max_length=50, null=True)),
                ('contract_terms', models.CharField(max_length=50)),
                ('account_officer', models.CharField(max_length=50, null=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supplier')),
            ],
        ),
    ]
