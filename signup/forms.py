from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    user_name = forms.CharField(max_length=100, required=False)
    user_surname = forms.CharField(max_length=100, required=False)
    user_email = forms.EmailField(max_length=100, required=False)
    user_phone_number = forms.CharField(max_length=100, required=False)
    user_login = forms.CharField(max_length=100, required=False)
    user_password = forms.CharField(max_length=100, required=False)
    user_password_again = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        widgets = {
            'user_password': forms.PasswordInput(),
            'user_password_again': forms.PasswordInput(),
        }
