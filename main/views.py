from django.shortcuts import render
from product.models import Product, UserData


def main(request):
    products = Product.objects.filter(is_main=True)
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    if not is_login and session_key:
        user_name = session_key
        try:
            kek = UserData.objects.get(owner_name=user_name)
            print(kek)
        except:
            UserData.objects.create(owner_name=user_name, liked_data='', order_data='')

    return render(request, 'main.html', locals())
