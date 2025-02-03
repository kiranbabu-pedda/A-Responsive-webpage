from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput, required=True)
