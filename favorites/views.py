from django.shortcuts import render
from signup.models import LikedProducts
from product.models import Product


def favorites(request, user_name):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    # ids = LikedProducts.objects.get(owner_name=user_name).liked_data
    ids = '6 7 8 9'
    ids = list(map(int, ids.split(' ')))
    new_ids = []
    favorite_products = []
    for id_prod in ids:
        try:
            favorite_products.append(Product.objects.get(id=id_prod))
            new_ids.append(str(id_prod))
        except:
            pass
    ids = ' '.join(new_ids)
    return render(request, 'favorites.html', locals())
