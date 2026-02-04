from django.urls import path
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('about/', TemplateView.as_view(
        template_name="firstapp/about.html",
        extra_context={"text": "Домашняя страница Django!"})),
    path('contact/', views.contact),
    path('details/', views.details),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
]
