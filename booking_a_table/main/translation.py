from modeltranslation.translator import register, TranslationOptions
from .models import Salats, HotDishes, SideDishesAndSoups, Drinks


@register(Salats)
class SalatsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(HotDishes)
class HotDishesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(SideDishesAndSoups)
class SideDishesAndSoupsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Drinks)
class DrinksTranslationOptions(TranslationOptions):
    fields = ('title',)
