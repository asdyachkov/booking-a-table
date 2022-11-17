from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def menu(request):
    return render(request, 'main/menu.html')


def rent_a_table(request):
    return render(request, 'main/rent_a_table.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def gallery(request):
    return render(request, 'main/gallery.html')
