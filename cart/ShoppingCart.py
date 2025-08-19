class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        shopping_cart = self.session.get('shopping_cart')

        if not shopping_cart:
            self.shopping_cart = self.session['shopping_cart'] = {}
        else:
            self.shopping_cart = shopping_cart


    def save_cart(self):
        self.session['shopping_cart'] = self.shopping_cart
        self.session.modified = True


    def clear_cart(self):
        self.session['shopping_cart'] = {}
        self.session.modified = True
        self.shopping_cart = {}


    def add_product(self, product):
        id_producto = str(product.cod_producto)

        if id_producto not in self.shopping_cart.keys():
            self.shopping_cart[id_producto] = {
                'nombre': product.nombre,
                'descripcion': product.descripcion,
                'precio': product.precio,
                'imagen': product.imagen.url,
                'cantidad': 1,
                'precio_acumulado': product.precio * 1
            }
        else:
            self.shopping_cart[id_producto]['cantidad'] += 1
            self.shopping_cart[id_producto]['precio_acumulado'] = product.precio * self.shopping_cart[id_producto]['cantidad']

        self.save_cart()


    def remove_product(self, product):
        id_producto = str(product.cod_producto)

        if id_producto in self.shopping_cart.keys():
            del self.shopping_cart[id_producto]
            self.save_cart()


    def subtract_product(self, product):
        id_producto = str(product.cod_producto)

        if id_producto in self.shopping_cart.keys():
            self.shopping_cart[id_producto]['cantidad'] -= 1
            self.shopping_cart[id_producto]['precio_acumulado'] -= product.precio

            if self.shopping_cart[id_producto]['cantidad'] <= 0:
                self.remove_product(product)

            self.save_cart()


    def get_total_price(self):
        total = 0
        for key, value in self.shopping_cart.items():
            if value['cantidad'] > 1:
                total += value['precio_acumulado']
            else:
                total += value['precio']
        return total


    def __str__(self):
        return f"ShoppingCart(items={self.shopping_cart})"