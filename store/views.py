from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from django.core.paginator import Paginator


class ProductList(ListView):
    model = Product
    context_object_name = 'categories'
    extra_context = {
        'title': 'Главная страница'
    }

    template_name = 'store/product_list.html'

    def get_queryset(self):
        categories = Category.objects.all()
        data = []
        for category in categories:
            products = Product.objects.filter(category=category, quantity__gt=0) # [:4]
            data.append({
                'title': category.title,
                'get_image_url': category.get_image_url,
                'products': products
            })

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.filter(quantity__gt=0).order_by('title')
        context['products'] = products
        return context


class ProductListByCategory(ListView):
    paginate_by = 32
    model = Product
    context_object_name = 'products'
    template_name = 'store/category_product_list.html'

    def get_queryset(self):
        # sort_field = self.request.GET.get('sort')

        products = Product.objects.filter(
            category_id=self.kwargs['pk'],
            quantity__gt=0
        )

        # if sort_field:
        #     products = products.order_by(sort_field)

        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'{category.title}'
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            super().dispatch(request, *args, **kwargs)
        except Http404:  # Импортируем
            return redirect('product_list')  # Импортируем

        return super().dispatch(request, *args, **kwargs)


class ProductListInCart(ListView):
    model = Product
    # context_object_name = ''
    template_name = 'store/cart.html'

    def get_queryset(self):
        products = Product.objects.filter(
            quantity__gt=0
        )

        # if sort_field:
        #     products = products.order_by(sort_field)

        return products



# def cart(request):
#     cart_info = get_cart_data(request)
#
#     context = {
#         'cart_total_quantity': cart_info['cart_total_quantity'],
#         'order': cart_info['order'],
#         'products': cart_info['products']
#     }
#
#     return render(request, 'store/cart.html', context)

#
# def to_cart(request, product_id, action):
#     user_cart = Cart(request, product_id, action)
#     return redirect('cart')
#
#
# def cart(request):
#     cart_data = get_cart_data(request)
#
#     context = {
#         'title': 'Оформление заказа',
#         'cart_total_quantity': cart_data['cart_total_quantity'],
#         'order': cart_data['order'],
#         'items': cart_data['products']
#     }
#     return render(request, 'store/cart.html', context)
