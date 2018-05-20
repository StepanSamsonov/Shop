from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'update_order', views.update_order, name='update_order'),
    url(r'order/', views.order, name='order'),
    url(r'checkout/', views.checkout, name='checkout'),
    url(r'success/', views.success, name='success'),
]
