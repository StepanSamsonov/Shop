from django.shortcuts import render
from product.models import *


def category(request, cat_name):
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

    if '_' in cat_name:
        cat_name = ' '.join(cat_name.split('_'))

    category = cat_name
    cat_list = Category.objects.all()
    res_cat = None
    for cat in cat_list:
        if cat.name == cat_name:
            res_cat = cat
            break
    prods = Product.objects.filter(category=res_cat.id)
    len_prods = len(prods)
    return render(request, 'category.html', locals())
