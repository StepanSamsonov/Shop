from django.shortcuts import render
from product.models import *
import sys


def product(request, product_id):
    product_ex = Product.objects.get(id=product_id)
    characteristic_lines = product_ex.characteristic.split('\n')
    description_lines = product_ex.description.split('\n')
    return render(request, 'product.html', locals())
