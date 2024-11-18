from modeltranslation.translator import register, TranslationOptions

from .models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'info')
