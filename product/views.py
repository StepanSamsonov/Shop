from django.shortcuts import render
from product.models import *
from order.views import str_to_dict
import random


def get_recommended(ind):
    users_data = UserData.objects.all()
    rec_products = set()
    popular_d = dict()
    count_of_showed = 6
    for elem in users_data:
        order_data = str_to_dict(elem.order_data)
        if ind in order_data:
            del order_data[ind]
            for element in order_data:
                rec_products.add(element)
                if element in popular_d:
                    popular_d[ind] += 1
                else:
                    popular_d[ind] = 1

    rec_products = list(rec_products)
    popular_ind = [ind for ind in popular_d]
    popular_ind.sort(key=lambda x: popular_d[x])
    popular_ind.reverse()
    recommends = set()
    while len(recommends) < count_of_showed and len(rec_products):
        rand_ind = random.randint(0, len(rec_products)-1)
        new_ind = rec_products[rand_ind]
        del rec_products[rand_ind]
        recommends.add(Product.objects.get(id=new_ind))

    while len(recommends) < count_of_showed and popular_ind:
        new_ind = popular_ind.pop(0)
        recommends.add(Product.objects.get(id=new_ind))

    id_list = [elem.id for elem in Product.objects.all()]
    del id_list[id_list.index(ind)]
    while len(recommends) < count_of_showed and len(id_list):
        rand_ind = random.randint(0, len(id_list) - 1)
        new_ind = id_list[rand_ind]
        del id_list[rand_ind]
        if rand_ind not in recommends:
            recommends.add(Product.objects.get(id=new_ind))
    return list(recommends)


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
    recommended_products = get_recommended(product_ex.id)
    return render(request, 'product.html', locals())
