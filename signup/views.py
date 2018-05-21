from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from product.models import UserData
from signup.forms import SignUpForm
from order.views import check_email, check_number


def signup(request):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    is_error = []

    user_login = ''
    user_name = ''
    user_surname = ''
    user_email = ''
    user_phone_number = ''

    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user_name = signup_form.cleaned_data['user_name']
            user_surname = signup_form.cleaned_data['user_surname']
            user_email = signup_form.cleaned_data['user_email']
            user_email = check_email(user_email)
            user_phone_number = signup_form.cleaned_data['user_phone_number']
            user_phone_number = check_number(user_phone_number)
            user_login = signup_form.cleaned_data['user_login']
            user_password = signup_form.cleaned_data['user_password']
            user_password_again = signup_form.cleaned_data['user_password_again']

            if not user_name:
                is_error.append('user_name')
            if not user_surname:
                is_error.append('user_surname')
            if not user_email and not user_phone_number:
                is_error.append('user_contacts')
            if not user_password or not user_password_again:
                is_error.append('user_passwords')

            users = User.objects.all()
            user_list = [elem.username for elem in users]

            if not user_login:
                is_error.append('user_login')
            elif user_login in user_list:
                is_error.append('user_login_exist')

            if user_password == user_password_again and not len(is_error):
                user = User.objects.create_user(user_login, user_email, user_password,
                                                first_name=user_name, last_name=user_surname)

                UserData.objects.create(owner_name=user_login, liked_data='', order_data='')
                login(request, user)
                return HttpResponseRedirect('/')
            elif user_password and user_password_again:
                is_error.append('different_passwords')
    else:
        signup_form = SignUpForm()

    return render(request, 'signup.html', locals())
