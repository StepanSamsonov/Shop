from django.shortcuts import render
from product.models import *


def order(request, order_data=''):
    return render(request, 'order.html', locals())
