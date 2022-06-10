from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'get_image')
    list_display_links = ('pk', 'title')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=65>')
        else:
            return '-'

    get_image.short_description = 'Миниатюра'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'price', 'quantity', 'get_photo')
    list_editable = ('price', 'quantity')
    list_display_links = ('pk', 'title')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=75>')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

# Register your models here.
