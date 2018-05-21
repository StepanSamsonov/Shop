from django.shortcuts import render
from product.models import Product, UserData
import random


def main(request):
    products_rec = Product.objects.filter(is_main=True)
    index_arr = set()
    while len(index_arr) != 4:
        index_arr.add(random.randint(0, len(products_rec)-1))
    index_arr = list(index_arr)
    products = []
    for ind in index_arr:
        products.append(products_rec[ind])

    is_login = request.user.is_authenticated()
    user_name = request.user.username

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if not is_login and session_key:
        user_name = session_key
        try:
            kek = UserData.objects.get(owner_name=user_name)
        except:
            UserData.objects.create(owner_name=user_name, liked_data='', order_data='')

    return render(request, 'main.html', locals())
