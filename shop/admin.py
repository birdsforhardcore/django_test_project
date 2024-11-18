from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import (Product, Category, Gallery, Review,
                     Mail, Customer, Order, OrderProduct, ShippingAddress)


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('pk', 'title', 'parent', 'get_products_count')
    prepopulated_fields = {'slug': ('title',)}

    def get_products_count(self, obj):
        if obj.products:
            return str(len(obj.products.all()))
        else:
            return '0'

    get_products_count.short_description = 'Количество товаров'


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('pk', 'title', 'category', 'quantity', 'price', 'created_at', 'size', 'color', 'get_photo')
    readonly_fields = ('watched',)
    list_editable = ('price', 'quantity', 'size', 'color')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'price')
    list_display_links = ('pk', 'title')
    inlines = (GalleryInline,)

    def get_photo(self, obj):
        if obj.images.all():
            return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'


admin.site.register(Gallery)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'created_at')
    readonly_fields = ('author', 'text', 'created_at')


@admin.register(Mail)
class ReviewMail(admin.ModelAdmin):
    """Почтовые подписки"""
    list_display = ('pk', 'mail', 'user')
    readonly_fields = ('mail', 'user')


@admin.register(Order)
class ReviewOrder(admin.ModelAdmin):
    """Корзина"""
    list_display = ('customer', 'created_at', 'is_completed', 'shipping')
    readonly_fields = ('customer', 'is_completed', 'shipping')
    list_filter = ('customer', 'is_completed')


@admin.register(Customer)
class ReviewCustomer(admin.ModelAdmin):
    """Заказчики"""
    list_display = ('user', 'first_name', 'last_name', 'email')
    readonly_fields = ('user', 'first_name', 'last_name', 'email', 'phone')
    list_filter = ('user',)


@admin.register(OrderProduct)
class ReviewOrderProduct(admin.ModelAdmin):
    """Товары в заказе"""
    list_display = ('product', 'order', 'quantity', 'added_at')
    readonly_fields = ('product', 'order', 'quantity', 'added_at')
    list_filter = ('product',)


@admin.register(ShippingAddress)
class ReviewShippingAddress(admin.ModelAdmin):
    """Адрес доставки"""
    list_display = ('customer', 'city', 'state', 'street', 'created_at')
    readonly_fields = ('customer', 'city', 'state', 'street', 'created_at')
    list_filter = ('customer', 'city', 'state', 'street')
