from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import Product, Supplier, Transaction, User
from app import models
import calculation

# Create your forms here.
class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact', 'address', 'email', 'bank_details']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class AddProductForm(forms.ModelForm):
    invoice_amount = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*unit_price')
    )
    class Meta:
        model = Product
        fields = ['supplier', 'description', 'quantity', 'unit_price', 'invoice_amount']
    
    

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['supplier', 'transaction_id', 'invoice_amount']


class PasswordResetForm(forms.Form):
    email = forms.EmailField()