from django.db import models
from django.utils.translation import gettext_lazy as _


class Salats(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    weight = models.IntegerField(verbose_name=_('Mass of the dish'))
    cost = models.IntegerField(verbose_name=_('The cost of the dish'))
    photo = models.TextField(verbose_name=_('Link to the image'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'
        ordering = ['title', 'weight', 'cost']


class HotDishes(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    weight = models.IntegerField(verbose_name=_('Mass of the dish'))
    cost = models.IntegerField(verbose_name=_('The cost of the dish'))
    photo = models.TextField(verbose_name=_('Link to the image'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Горячее блюдо'
        verbose_name_plural = 'Горячие блюда'
        ordering = ['title', 'weight', 'cost']


class SideDishesAndSoups(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    weight = models.IntegerField(verbose_name=_('Mass of the dish'))
    cost = models.IntegerField(verbose_name=_('The cost of the dish'))
    photo = models.TextField(verbose_name=_('Link to the image'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Гарнир или суп'
        verbose_name_plural = 'Гарниры и супы'
        ordering = ['title', 'weight', 'cost']


class Drinks(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    weight = models.IntegerField(verbose_name=_('Mass of the dish'))
    cost = models.IntegerField(verbose_name=_('The cost of the dish'))
    photo = models.TextField(verbose_name=_('Link to the image'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'
        ordering = ['title', 'weight', 'cost']


class RentATable(models.Model):
    client_name = models.CharField('Имя клиента', max_length=100)
    clients_count = models.IntegerField('Количество гостей')
    date = models.DateField('Дата прихода гостей')
    time = models.TimeField('Время прихода гостей')
    phone_number = models.CharField('Номер телефона клиента', max_length=16)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['client_name', 'clients_count', 'date', 'time']


class PhotoLinks(models.Model):
    link = models.CharField('Ссылка на фото', max_length=250)

    def __str__(self):
        return 'Ссылка'

    class Meta:
        verbose_name = 'Ссылка на фото'
        verbose_name_plural = 'Ссылки на фото'
