from django import template
from shop.models import Category, FavoriteProducts, Order, Customer
from django.template.defaulttags import register as range_register


register = template.Library()


@register.simple_tag()
def get_subcategories(category):
    return Category.objects.filter(parent=category)


@register.simple_tag()
def get_sorted():
    sorters = [
        {
            'title': 'Цена',
            'sorters': [
                ('price', 'по возрастанию'),
                ('-price', 'по убыванию')
            ]
        },
        {
            'title': 'Цвет',
            'sorters': [
                ('color', 'от А до Я'),
                ('-color', 'от Я до А')
            ]
        },
        {
            'title': 'Размер',
            'sorters': [
                ('size', 'по возрастанию'),
                ('-size', 'по убыванию')
            ]
        }
    ]
    return sorters


@range_register.filter
def get_positive_range(value):
    return range(int(value))


@range_register.filter
def get_negative_range(value):
    return range(5 - int(value))


@register.simple_tag()
def get_favorite_products(user):
    """Вывод избранных товаров"""
    fav = FavoriteProducts.objects.filter(user=user)
    products = [i.product for i in fav]
    return products


@register.simple_tag()
def get_basket_count(user):
    """Вывод количества товаров в корзине"""
    customer = Customer.objects.get(user=user)
    basket = Order.objects.get(customer=customer)
    return basket.get_cart_total_quantity


@register.simple_tag()
def get_favorite_count(user):
    """Вывод количества товаров в избранном"""
    return len(get_favorite_products(user))
