from django import forms
from .models import Order


class CheckoutForm(forms.Form):
    customer_address = forms.CharField(max_length=200, required=False)
    customer_comments = forms.CharField(widget=forms.Textarea, required=False)
    customer_first_name = forms.CharField(max_length=200, required=True)
    customer_second_name = forms.CharField(max_length=200, required=True)
    customer_email = forms.CharField(max_length=200, required=True)
    customer_number = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Order
