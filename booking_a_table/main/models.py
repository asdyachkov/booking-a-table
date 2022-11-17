from django.db import models


class Salats(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Масса блюда')
    cost = models.IntegerField('Стоимость блюда')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return 'Салаты'

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'


class HotDishes(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Масса блюда')
    cost = models.IntegerField('Стоимость блюда')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return 'Горячие блюда'

    class Meta:
        verbose_name = 'Горячие блюда'
        verbose_name_plural = 'Горячее блюдо'


class SideDishesAndSoups(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Масса блюда')
    cost = models.IntegerField('Стоимость блюда')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return 'Гарниры и супы'

    class Meta:
        verbose_name = 'Гарниры и супы'
        verbose_name_plural = 'Гарнир или суп'


class Drinks(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Объем напитка')
    cost = models.IntegerField('Стоимость напитка')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return 'Напитки'

    class Meta:
        verbose_name = 'Напитки'
        verbose_name_plural = 'Напиток'
