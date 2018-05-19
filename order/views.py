from django.shortcuts import render
from product.models import Product, UserData
from django.http import JsonResponse


def str_to_dict(s):
    d = dict()
    if s != '':
        s = s.split(' ')
        for elem in s:
            a, b = map(int, elem.split(':'))
            d[a] = b
    return d


def dict_to_str(d):
    s = []
    for elem in d:
        s.append(str(elem) + ':' + str(d[elem]))
    return ' '.join(s)


def update_order(request):
    post = request.POST.dict()
    user_name = request.user.username
    user_data = UserData.objects.get(owner_name=user_name).order_data
    user_data_d = str_to_dict(user_data)

    if post['is_delete'] == 'false':
        user_data_d[int(post['product_id'])] = int(post['count'])
    else:
        del user_data_d[int(post['product_id'])]

    user_data = dict_to_str(user_data_d)
    user = UserData.objects.get(owner_name=user_name)
    user.order_data = user_data
    user.save(update_fields=['order_data'])
    return JsonResponse(dict())


def order(request, user_name):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    data = UserData.objects.get(owner_name=user_name).order_data
    data_d = str_to_dict(data)
    correct_order = len(data_d) > 0

    new_data = []
    order_dict = dict()
    for id_prod in data_d:
        try:
            order_dict[Product.objects.get(id=id_prod)] = data_d[id_prod]
        except:
            del data_d[id_prod]

    new_data = dict_to_str(data_d)
    data = UserData.objects.get(owner_name=user_name)
    data.order_data = new_data
    data.save(update_fields=['order_data'])
    return render(request, 'order.html', locals())
