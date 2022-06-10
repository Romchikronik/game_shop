from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Категория')
    image = models.ImageField(upload_to='category_photos/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_list_by_category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Category(pk={self.pk}, title={self.title})'

    @property  # Получение
    def get_image_url(self):
        try:
            url = self.image.url
        except:
            url = 'https://st.depositphotos.com/1001925/2675/i/950/depositphotos_26757465-stock-photo-background-of-aged-grungy-textured.jpg'
        return url

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['pk']


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='product_photos/', null=True, blank=True, verbose_name='Изображение')
    # null=True - необязательное в бд, blank=True - необязательное для заполнения
    quantity = models.IntegerField(default=0, verbose_name='Количество')  # на складе нужно убрать кажется
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def add_to_card(self):
        return reverse('to_cart', kwargs={'product_id': self.pk, 'action': 'add'})


    # def get_absolute_url(self):
    #     return reverse('product_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Product(pk={self.pk}, title={self.title})'

    @property  # Получение
    def get_image_url(self):
        try:
            url = self.image.url
        except:
            url = 'https://st.depositphotos.com/1001925/2675/i/950/depositphotos_26757465-stock-photo-background-of-aged-grungy-textured.jpg'
        return url

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category']


# class Order(models.Model):
#     customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Покупатель')
#
#     def __str__(self):
#         return str(self.pk)
#
#     @property
#     def get_cart_total_price(self):
#         order_products = self.orderproduct_set.all()
#         total_price = sum([product.get_total_price for product in order_products])
#         return total_price
#
#     @property
#     def get_cart_total_quantity(self):
#         order_products = self.orderproduct_set.all()
#         total_quantity = sum([product.quantity for product in order_products])
#         return total_quantity
#
#     class Meta:
#         verbose_name = 'Заказ'
#         verbose_name_plural = 'Заказы'
#
#
# class OrderProduct(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='Продукт')
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name='Заказ')
#     quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='Количество')
#     # total_sum = models.IntegerField(default=0, null=True, blank=True, verbose_name='Сумма')
#
#     @property
#     def get_total_price(self):
#         total_price = self.product.price * self.quantity
#         return total_price  # Возвращаем общую сумму товаров в корзине
#
#     class Meta:
#         verbose_name = 'Товар в заказе'
#         verbose_name_plural = 'Товары в заказах'
    


