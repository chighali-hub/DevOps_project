from django import forms
from .models import Members


# creating a form
class Memberform(forms.ModelForm):

    # create meta class
    class Meta:
        model = Members
        fields = ['name', 'email', 'contact', 'address', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Name', 'maxlength': 255,'required':'required'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Email','required':'required'}),
            'contact': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Contact','required':'required'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder': 'Address','required':'required'}),
            'gender': forms.TextInput(attrs={'class':'form-control','placeholder': 'Gender', 'maxlength': 255,'required':'required'}),
        }


      