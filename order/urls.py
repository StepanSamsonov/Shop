from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'order/(?P<user_name>.*)/$', views.order, name='order')
]
