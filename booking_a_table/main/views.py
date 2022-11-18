from django.shortcuts import render, redirect
from .models import Salats, SideDishesAndSoups, HotDishes, Drinks, PhotoLinks
from .forms import RentATableForm


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
    error = ''
    if request.method == 'POST':
        form = RentATableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена неверно'

    form = RentATableForm()
    data = {'form': form, 'error': error}
    return render(request, 'main/rent_a_table.html', data)


def contacts(request):
    return render(request, 'main/contacts.html')


def gallery(request):
    photos = PhotoLinks.objects.all()
    return render(request, 'main/gallery.html', {'photos': photos})
