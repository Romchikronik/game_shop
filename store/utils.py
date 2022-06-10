# from django.contrib.auth.models import User
#
# from .models import Order, OrderProduct, Product
# from megashop import settings
#
#
#
# class Cart:
#     def __init__(self, request, product_id=None, action=None):
#         self.session = request.session
#         self.cart = self.get_cart()
#
#         if product_id and action:
#             self.key = str(product_id)
#             self.product = Product.objects.get(pk=product_id)
#             self.cart_product = self.cart.get(self.key)
#
#             if action == 'add' and self.product.quantity > 0:
#                 self.add()
#             elif action == 'delete':
#                 self.delete()
#
#             self.product.save()
#             self.save()
#
#     def get_cart(self):
#         cart = self.session['cart'] = {}
#         return cart
#
#     def save(self):
#         self.session.modified = True
#
#     def get_cart_info(self):
#         products = []
#         order = {
#             'get_cart_total_price': 0,
#             'get_cart_total_quantity': 0
#         }
#
#         cart_total_quantity = order['get_cart_total_quantity']
#         cart_total_price = order['get_cart_total_price']
#
#         for key in self.cart:
#             if self.cart[key]['quantity'] > 0:
#                 product_quantity = self.cart[key]['quantity']
#                 cart_total_quantity += product_quantity
#                 product = Product.objects.get(pk=key)
#
#                 get_total_price = product.price * product_quantity
#
#                 cart_product = {
#                     'pk': product.pk,
#                     'product': {
#                         'pk': product.pk,
#                         'title': product.title,
#                         'price': product.price,
#                         'get_image_url': product.get_image_url,
#                         'quantity': product.quantity
#                     },
#                     'quantity': product_quantity,
#                     'get_total_price': get_total_price
#                 }
#
#                 products.append(cart_product)
#                 order['get_cart_total_price'] += cart_product['get_total_price']
#                 order['get_cart_total_quantity'] += cart_product['quantity']
#                 cart_total_price = order['get_cart_total_price']
#         self.save()
#
#         return {
#             'cart_total_quantity': cart_total_quantity,
#             'cart_total_price': cart_total_price,
#             'order': order,
#             'products': products
#         }
#
#     def add(self):
#         if self.cart_product:
#             self.cart_product['quantity'] += 1
#         else:
#             self.cart[self.key] = {
#                 'quantity': 1
#             }
#         self.product.quantity -= 1
#
#     def delete(self):
#         self.cart_product['quantity'] -= 1
#         self.product.quantity += 1
#
#         if self.cart_product['quantity'] <= 0:
#             del self.cart[self.key]
#
#     def clear(self):
#         self.cart.clear()
#
#
# def get_cart_data(request):
#     session_cart = Cart(request)
#     cart_info = session_cart.get_cart_info()
#
#     return {
#         'cart_total_quantity': cart_info['cart_total_quantity'],
#         'cart_total_price': cart_info['cart_total_price'],
#         'order': cart_info['order'],
#         'products': cart_info['products']
#     }
#
#
# def anonymous_order(request):
#     cart = Cart(request)
#     cart_info = cart.get_cart_info()
#     items = cart_info['products']
#     order = Order.objects.create(user=User)
#
#     for item in items:
#         product = Product.objects.get(pk=item['pk'])
#         OrderProduct.objects.create(
#             product=product,
#             order=order,
#             quantity=item['quantity']
#         )
#
#     return order
