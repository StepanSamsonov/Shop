from django.shortcuts import render
from product.models import Product


def main(request):
    products = Product.objects.filter(is_active=True, is_main=True)
    return render(request, 'main.html', locals())
