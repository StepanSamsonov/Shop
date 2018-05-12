from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'order/', views.order, name='order')
]
