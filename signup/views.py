from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from signup.forms import SignUpForm
from signup.models import UserAddedData


def signup(request):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user_name = signup_form.cleaned_data['user_name']
            user_surname = signup_form.cleaned_data['user_surname']
            user_email = signup_form.cleaned_data['user_email']
            user_phone_number = signup_form.cleaned_data['user_phone_number']
            user_login = signup_form.cleaned_data['user_login'].lower()
            user_password = signup_form.cleaned_data['user_password']
            user_password_again = signup_form.cleaned_data['user_password_again']

            users = User.objects.all()
            user_list = [elem.username for elem in users]

            if user_login in user_list:
                return HttpResponseRedirect('/signup')

            elif user_password == user_password_again:
                user = User.objects.create_user(user_login, user_email, user_password,
                                                first_name=user_name, last_name=user_surname)

                # UserAddedData.objects.create(owner_name=user_login, liked_data='', order_data='')
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/signup')
    else:
        signup_form = SignUpForm()

    return render(request, 'signup.html', locals())
