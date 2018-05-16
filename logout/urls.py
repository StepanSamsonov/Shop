from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^logout', views.logout_user, name='logout')
]
