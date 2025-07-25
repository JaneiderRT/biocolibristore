from django.shortcuts import render, redirect
from django.http import JsonResponse

from core.models import Producto
from .ShoppingCart import ShoppingCart

# Create your views here.
def cart_view(request):
    cart = ShoppingCart(request)
    total_price = cart.get_total_price() if cart.shopping_cart else 0
    return render(request, 'cart/cart.html', {'cart': cart.shopping_cart, 'total_price': total_price})


def add_to_cart(request, product_id):
    cart = ShoppingCart(request)
    product = Producto.objects.get(cod_producto=product_id)
    cart.add_product(product)
    return redirect('cart_view')


def subtract_from_cart(request, product_id):
    cart = ShoppingCart(request)
    product = Producto.objects.get(cod_producto=product_id)
    cart.subtract_product(product)
    return redirect('cart_view')


def remove_product_cart(request, product_id):
    cart = ShoppingCart(request)
    product = Producto.objects.get(cod_producto=product_id)
    cart.remove_product(product)
    return redirect('cart_view')


def clear_cart(request):
    cart = ShoppingCart(request)
    cart.clear_cart()
    return redirect('cart_view')