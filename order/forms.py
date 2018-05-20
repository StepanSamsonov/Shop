from django import forms
from .models import Order


class CheckoutForm(forms.Form):
    customer_address = forms.CharField(max_length=200, required=False)
    customer_comments = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Order
