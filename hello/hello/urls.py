from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('details/', views.details),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
]
