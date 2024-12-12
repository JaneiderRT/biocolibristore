from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singup/', views.singup, name='singup'),
    path('singin/', views.singin, name='singin'),
    path('singout/', views.singout, name='singout'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:id>/', views.product_view, name='product_view'),
    path('about_us/', views.about_us, name='about_us')
]
