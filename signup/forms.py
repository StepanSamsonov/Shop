from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    user_name = forms.CharField(max_length=100, required=True)
    user_surname = forms.CharField(max_length=100, required=True)
    user_email = forms.EmailField(max_length=100, required=True)
    user_phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    user_login = forms.CharField(max_length=100, required=True)
    user_password = forms.CharField(max_length=100, required=True)
    user_password_again = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        widgets = {
            'user_password': forms.PasswordInput(),
            'user_password_again': forms.PasswordInput(),
        }
