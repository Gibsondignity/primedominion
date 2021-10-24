from django.db import models
from django.db.models.fields import DecimalField
from django.db.models.fields.related import ForeignKey
from django.forms.models import BaseInlineFormSet
from app.models import Supplier, Contract
from django.db.models.deletion import CASCADE
#import computed_property
from datetime import datetime



# Create your models here.
class AccountantUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



class Accountant(models.Model):
    status = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
        ('Part Payment', 'Part Payment'),
    )
    payment_status = models.CharField(max_length=50, choices=status)
    invoice_amount = models.DecimalField(max_digits=9, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=CASCADE, max_length=50, null=True)
    swift_code = models.CharField(max_length=50, null=True, blank=True)
    balance_due = models.DateField(default=datetime.now(), blank=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    


    def __str__(self):
        return f'Supplier: {self.supplier} - Statuse: {self.payment_status}'