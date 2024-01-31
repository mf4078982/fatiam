from django import forms
from .models import My_model


class My_f(forms.ModelForm):
    class Meta:
        model = My_model
        fields = ['id','name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }