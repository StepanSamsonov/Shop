from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'update_order', views.update_order, name='update_order'),
    url(r'order/(?P<user_name>.*)/$', views.order, name='order'),
]
