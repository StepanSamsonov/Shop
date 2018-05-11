from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^product/(?P<product_id>.*)/$', views.product, name='product')
]
