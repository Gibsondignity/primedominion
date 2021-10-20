from django.db import models
from django.db.models.fields import DecimalField
from django.db.models.fields.related import ForeignKey
from app.models import Supplier, Contract
from django.db.models.deletion import CASCADE

# Create your models here.
class Accountant(models.Model):
    status = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
        ('Part Payment', 'Part Payment'),
    )
    payment_status = models.DecimalField(max_digits=9, decimal_places=2, choices=status)
    amount_paid = DecimalField(max_digits=9, decimal_places=2, null=True)
    balace = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    #due_date = models.ForeignKey(Contract.due_date, on_delete=CASCADE)
    supplier = ForeignKey(Supplier, on_delete=CASCADE, max_length=50, null=True)
    #swift_code = models.ForeignKey(Supplier.swift_code, on_delete=CASCADE, null=True)
    invoice_amount = models.DecimalField(max_digits=9, decimal_places=2)

    

    def __str__(self):
        return f'Supplier: {self.Supplier} - Statuse: {self.payment_status}'