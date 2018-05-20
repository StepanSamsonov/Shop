from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^update_favorites', views.update_favorites, name='update_favorites'),
    url(r'^favorites/', views.favorites, name='favorites'),
]
