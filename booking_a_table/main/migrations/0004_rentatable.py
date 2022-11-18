# Generated by Django 4.1.3 on 2022-11-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_drinks_hotdishes_sidedishesandsoups'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentATable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100, verbose_name='Имя клиента')),
                ('clients_count', models.IntegerField(verbose_name='Количество гостей')),
                ('date', models.DateField(verbose_name='Дата прихода гостей')),
                ('time', models.TimeField(verbose_name='Время прихода гостей')),
                ('phone_number', models.CharField(max_length=16, verbose_name='Имя клиента')),
            ],
            options={
                'verbose_name': 'Бронирования',
                'verbose_name_plural': 'Бронирование',
            },
        ),
    ]
