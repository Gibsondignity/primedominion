from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import Product, Supplier, Transaction
from app import models

# Create your forms here.
class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact', 'address', 'email', 'bank_details']


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['supplier', 'description', 'quantity', 'invoice_amount']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['supplier', 'transaction_id', 'invoice_amount', 'description']

        