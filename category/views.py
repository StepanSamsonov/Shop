from django.shortcuts import render
from product.models import *


def category(request, cat_name):
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
