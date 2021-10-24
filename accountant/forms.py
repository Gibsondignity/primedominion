from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import *
from . import models




class AddContractForm(forms.ModelForm):
    class Meta:
        model = Accountant
        
        fields = '__all__'
    
        widgets = {
            
            "payment_status": forms.Select(attrs={'class': 'form-control'}),
            "amount_paid": forms.TextInput(attrs={'class': 'form-control amount'}),
            "supplier": forms.Select(attrs={'class': 'form-control'}),
            "invoice_amount": forms.TextInput(attrs={'class': 'form-control invoice'}),
            "balance_due": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "swift_code": forms.TextInput(attrs={'class': 'form-control'}),
            "balance": forms.TextInput(attrs={'class': 'form-control balance'}),

        }


