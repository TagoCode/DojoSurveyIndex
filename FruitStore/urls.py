from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('goto', views.func)
]

