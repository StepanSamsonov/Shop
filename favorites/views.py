from django.http import JsonResponse
from django.shortcuts import render
from product.models import Product, UserData


def update_favorites(request):
    post = request.POST.dict()
    user_name = request.user.username
    user_data = UserData.objects.get(owner_name=user_name).liked_data
    if user_data != '':
        user_data = user_data.split(' ')
    else:
        user_data = []

    if post['is_delete'] == 'false':
        if post['product_id'] not in user_data:
            user_data.append(post['product_id'])
    else:
        del user_data[user_data.index(post['product_id'])]

    user_data = ' '.join(user_data)
    user = UserData.objects.get(owner_name=user_name)
    user.liked_data = user_data
    user.save(update_fields=['liked_data'])
    return JsonResponse(dict())


def favorites(request):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    ids = UserData.objects.get(owner_name=user_name).liked_data
    if ids != '':
        ids = list(map(int, ids.split(' ')))
    else:
        ids = []

    len_user_data = len(ids)
    new_ids = []
    favorite_products = []
    for id_prod in ids:
        try:
            favorite_products.append(Product.objects.get(id=id_prod))
            new_ids.append(str(id_prod))
        except:
            pass
    ids = ' '.join(new_ids)
    data = UserData.objects.get(owner_name=user_name)
    data.liked_data = ids
    data.save(update_fields=['liked_data'])
    return render(request, 'favorites.html', locals())
