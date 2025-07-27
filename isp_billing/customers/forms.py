from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'tin', 'phone', 'email', 'address', 'nic_or_passport', 'is_active']
