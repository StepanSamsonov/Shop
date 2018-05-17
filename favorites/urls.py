from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^favorites/(?P<user_name>.*)/$', views.favorites, name='favorites')
]
