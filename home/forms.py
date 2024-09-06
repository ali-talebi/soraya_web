from .models import ContactUs
from django import forms


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'family', 'email', 'phone', 'text']



