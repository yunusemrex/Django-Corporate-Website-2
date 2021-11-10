  
from django import forms
from cosmosit.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name','subject','email', 'message',)