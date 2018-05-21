from django.shortcuts import render
from product.models import *


def product(request, product_id):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if not is_login:
        user_name = session_key
        try:
            UserData.objects.get(owner_name=user_name)
        except:
            UserData.objects.create(owner_name=user_name, liked_data='', order_data='')

    product_ex = Product.objects.get(id=product_id)
    characteristic_lines = product_ex.characteristic.split('\n')
    description_lines = product_ex.description.split('\n')
    return render(request, 'product.html', locals())
