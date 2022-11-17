from django.shortcuts import render
from .models import Salats, SideDishesAndSoups, HotDishes, Drinks


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def menu(request):
    salats = Salats.objects.all()
    sideDishesAndSoups = SideDishesAndSoups.objects.all()
    hotDishes = HotDishes.objects.all()
    drinks = Drinks.objects.all()
    return render(request, 'main/menu.html', {'salats': salats, 'sideDishesAndSoups': sideDishesAndSoups, 'hotDishes': hotDishes, 'drinks': drinks})


def rent_a_table(request):
    return render(request, 'main/rent_a_table.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def gallery(request):
    return render(request, 'main/gallery.html')
