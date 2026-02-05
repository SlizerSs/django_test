from django.urls import path
from firstapp import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('about/', TemplateView.as_view(
        template_name="firstapp/about.html",
        extra_context={"text": "Домашняя страница Django!"})),
    path('contact/', views.contact),
    path('details/', views.details),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
]
