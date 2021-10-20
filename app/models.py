from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields, manager
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField, FloatField
from django.db.models.fields.related import ForeignKey
from django.db.utils import DatabaseError


#from app.views import transactions

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=50, help_text='Enter your full name')
    contact = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length = 50, help_text="Enter your email address")
    bank_details = models.CharField(max_length=200, help_text='Summary of bank details', null=True)
    Bank_name = models.CharField(max_length=50, null=True)
    Bank_address = models.CharField(max_length=50, null=True)
    Bank_account_name = models.CharField(max_length=50, null=True)
    Bank_account_number = models.CharField(max_length=50, null=True)
    swift_code = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
 


class Contract(models.Model):
    
    terms = (
        ('30-70%', '30-70%'),
        ('50-50%', '50-50%'),
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Credit', 'Credit'),
    )
    invoice_number = models.CharField(max_length=50, null=50)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=CASCADE)
    invoice_amount = models.DecimalField(max_digits=9, decimal_places=2)
    product_name = models.CharField(max_length=50, null=True)
    contract_terms = models.CharField(max_length=50, choices=terms)
    account_officer = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Supplier: {self.supplier} - Product: {self.product_name}'


