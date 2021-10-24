# Generated by Django 3.2.7 on 2021-10-21 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_alter_contract_contract_terms'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountantUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.DecimalField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid'), ('Part Payment', 'Part Payment')], decimal_places=2, max_digits=9)),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=9, null=True)),
                ('balace', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('swift_code', models.CharField(blank=True, max_length=50, null=True)),
                ('supplier', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.supplier')),
            ],
        ),
    ]