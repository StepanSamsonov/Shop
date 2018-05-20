from django.shortcuts import render
from product.models import Product, UserData
from .models import Order, ProductInOrder, OrderStatus
from django.http import JsonResponse, HttpResponseRedirect
from .forms import CheckoutForm


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


def order(request):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    data = UserData.objects.get(owner_name=user_name).order_data
    data_d = str_to_dict(data)
    len_order_data = len(data_d)
    correct_order = len(data_d) > 0

    new_data = []
    order_dict = dict()
    total_order_price = 0
    for id_prod in data_d:
        try:
            loc_prod = Product.objects.get(id=id_prod)
            order_dict[loc_prod] = data_d[id_prod]
            total_order_price += data_d[id_prod]*loc_prod.price
        except:
            del data_d[id_prod]

    new_data = dict_to_str(data_d)
    data = UserData.objects.get(owner_name=user_name)
    data.order_data = new_data
    data.save(update_fields=['order_data'])
    return render(request, 'order.html', locals())


def checkout(request):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    user_data = UserData.objects.get(owner_name=user_name)
    product_d = str_to_dict(user_data.order_data)
    total_order_price = 0
    for id_prod in product_d:
        loc_prod = Product.objects.get(id=id_prod)
        total_order_price += product_d[id_prod]*loc_prod.price

    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            address = checkout_form.cleaned_data['customer_address']
            comments = checkout_form.cleaned_data['customer_comments']
            user = request.user
            customer_name = user.first_name + ' ' + user.last_name
            phone_number = user_data.phone_number
            email = user.email
            order_status = OrderStatus.objects.get(name='Новый')
            new_order = Order(customer_name=customer_name, customer_email=email, customer_phone=phone_number,
                          customer_address=address, comments=comments, status=order_status)
            new_order.save()

            for prod_id in product_d:
                product = Product.objects.get(id=prod_id)
                product_in_order = ProductInOrder(order=new_order, product=product, price_per_one=product.price,
                                                  number=product_d[prod_id])
                product_in_order.save()

            return HttpResponseRedirect('/success')
        else:
            return HttpResponseRedirect('/checkout')

    return render(request, 'checkout.html', locals())


def success(request):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    return render(request, 'success.html', locals())
