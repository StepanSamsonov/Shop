from django.shortcuts import render
from product.models import Product


def main(request):
    products = Product.objects.filter(is_main=True)
    is_login = request.user.is_authenticated()
    return render(request, 'main.html', locals())
