from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/<int:pk>/', ProductListByCategory.as_view(), name='product_list_by_category'),

    path('cart/', ProductListInCart.as_view(), name='cart')
    # path('cart/', cart, name='cart'),
    # # path('checkout/', checkout, name='checkout'),
    # path('to_cart/<int:product_id>/<str:action>', to_cart, name='to_cart')
]
