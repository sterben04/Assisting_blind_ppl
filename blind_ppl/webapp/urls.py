from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('get_image/', views.get_image), 
    path('get_lang/', views.get_regional_lang)
]