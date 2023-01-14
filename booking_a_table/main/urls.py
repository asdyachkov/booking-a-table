from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('rent_a_table', views.rent_a_table, name='rent_a_table'),
    path('contacts', views.contacts, name='contacts'),
    path('gallery', views.gallery, name='gallery')
]
