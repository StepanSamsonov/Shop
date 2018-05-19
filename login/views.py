from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from login.forms import LogInForm
from django.contrib.auth import authenticate, login


def login_user(request):
    is_login = request.user.is_authenticated()
    user_name = request.user.username

    if request.method == 'POST':
        signup_form = LogInForm(request.POST)
        if signup_form.is_valid():
            user_login = signup_form.cleaned_data['user_login']
            user_password = signup_form.cleaned_data['user_password']
            user = authenticate(username=user_login, password=user_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')

        else:
            return HttpResponseRedirect('/login')

    else:
        signup_form = LogInForm()

    return render(request, 'login.html', locals())
