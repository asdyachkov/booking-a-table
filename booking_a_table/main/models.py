from django.db import models


class Salats(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Масса блюда')
    cost = models.IntegerField('Стоимость блюда')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Салат'
        verbose_name_plural = 'Салаты'


class HotDishes(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Масса блюда')
    cost = models.IntegerField('Стоимость блюда')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Горячие блюда'
        verbose_name_plural = 'Горячее блюдо'


class SideDishesAndSoups(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Масса блюда')
    cost = models.IntegerField('Стоимость блюда')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Гарниры и супы'
        verbose_name_plural = 'Гарнир или суп'


class Drinks(models.Model):
    title = models.CharField('Название', max_length=100)
    weight = models.IntegerField('Объем напитка')
    cost = models.IntegerField('Стоимость напитка')
    photo = models.TextField('Ссылка на изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Напитки'
        verbose_name_plural = 'Напиток'


class RentATable(models.Model):
    client_name = models.CharField('Имя клиента', max_length=100)
    clients_count = models.IntegerField('Количество гостей')
    date = models.DateField('Дата прихода гостей')
    time = models.TimeField('Время прихода гостей')
    phone_number = models.CharField('Имя клиента', max_length=16)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Бронирования'
        verbose_name_plural = 'Бронирование'
