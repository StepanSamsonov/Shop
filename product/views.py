from django.shortcuts import render
from product.models import *


def product(request, product_id):
    is_login = request.user.is_authenticated()

    product_ex = Product.objects.get(id=product_id)
    characteristic_lines = product_ex.characteristic.split('\n')
    description_lines = product_ex.description.split('\n')
    return render(request, 'product.html', locals())
