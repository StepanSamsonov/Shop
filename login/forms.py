from django import forms
from django.contrib.auth.models import User


class LogInForm(forms.Form):
    user_login = forms.CharField(max_length=100, required=True)
    user_password = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        widgets = {
            'user_password': forms.PasswordInput(),
        }
