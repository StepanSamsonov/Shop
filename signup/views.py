from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from signup.forms import SignUpForm


def signup(request):

    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user_name = signup_form.cleaned_data['user_name']
            user_surname = signup_form.cleaned_data['user_surname']
            user_email = signup_form.cleaned_data['user_email']
            user_phone_number = signup_form.cleaned_data['user_phone_number']
            user_login = signup_form.cleaned_data['user_login']
            user_password = signup_form.cleaned_data['user_password']
            user_password_again = signup_form.cleaned_data['user_password_again']
            if user_password == user_password_again:
                user = User.objects.create_user(user_login, user_email, user_password,
                                                first_name=user_name, last_name=user_surname)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/signup')
    else:
        signup_form = SignUpForm()

    return render(request, 'signup.html', locals())
