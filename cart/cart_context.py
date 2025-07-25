def cart_product_count(request):
    cart = request.session.get('shopping_cart', {})
    total_products = sum(product.get('cantidad', 0) for product in cart.values())
    return {'cart_product_count': total_products}