from django.shortcuts import render
from product.models import *


def order(request, order_data=''):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    return render(request, 'order.html', locals())
