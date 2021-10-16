from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

#from app.views import transactions

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200, help_text='Enter your full name')
    contact = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length = 150, help_text="Enter your email address")
    bank_details = models.CharField(max_length=200)


    def __str__(self):
        return self.name
 


class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    invoice_amount = models.FloatField()

    
    def __str__(self):
        return self.supplier.name

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=25)
    invoice_date = models.DateTimeField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    invoice_number = models.FloatField()
    product_name = models.CharField(max_length=30)

    def __str__(self):
        return self.invoice_number



class Transaction(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=40)
    invoice_amount = models.FloatField()
    #contract terms

    
    def __str__(self):
        return self.transaction_id

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username




