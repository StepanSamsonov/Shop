from django.shortcuts import render
from signup.models import UserAddedData
from product.models import Product


def order(request, user_name):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    # data = UserAddedData.objects.get(owner_name=user_name).order_data
    data = '6:2 7:1 8:5 9:1'
    data = data.split(' ')
    data_d = dict()
    for elem in data:
        id_p, count = map(int, elem.split(':'))
        data_d[id_p] = count

    new_data = []
    order_dict = dict()
    for id_prod in data_d:
        try:
            order_dict[Product.objects.get(id=id_prod)] = data_d[id_prod]
            new_data.append(str(id_prod) + ':' + str(data_d[id_prod]))
        except:
            pass
    ids = ' '.join(new_data)
    return render(request, 'order.html', locals())
