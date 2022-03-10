from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get_image/', views.get_image), 
]