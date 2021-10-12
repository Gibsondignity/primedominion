from django import forms
from django.forms.forms import Form
from .models import Product, Supplier

# Create your forms here.
class AddSupplierForm(forms.Form):
    class Meta:
        model = Supplier
        fields = ['name', 'contact', 'address', 'email', 'bank_details']


class AddProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['supplier', 'description', 'quantity', 'invoice_amount']