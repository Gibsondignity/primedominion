from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import Supplier, Contract
from app import models


# Create your forms here.
class AddSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'



class AddContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
    
        widgets = {
            "invoice_number": forms.TextInput(attrs={'class': 'form-control'}),
            "start_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "due_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "supplier": forms.Select(attrs={'class': 'form-control'}),
            "invoice_amount": forms.TextInput(attrs={'class': 'form-control'}),
            "product_name": forms.TextInput(attrs={'class': 'form-control'}),
            "contract_terms": forms.Select(attrs={'class': 'form-control'}),
            
        }
    



class PasswordResetForm(forms.Form):
    email = forms.EmailField()