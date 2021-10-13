from django import forms
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200, help_text='Enter your full name')
    contact = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length = 150, help_text="")
    bank_details = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Product(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    invoice_amount = models.FloatField()

    def __str__(self):
        return self.supplier.name



class Transaction(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=40)
    invoice_amount = models.FloatField()
    description = models.TextField()


    def __str__(self):
        return f'{self.transaction_id}'


class Payment(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    amount = models.FloatField()










