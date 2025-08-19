from django.urls import path

from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/subtract/<int:product_id>/', views.subtract_from_cart, name='subtract_from_cart'),
    path('cart/remove/<int:product_id>/', views.remove_product_cart, name='remove_product_cart'),
    path('cart/clear/', views.clear_cart, name='clear_cart'),
]