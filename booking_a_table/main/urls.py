from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('menu', views.menu),
    path('rent_a_table', views.rent_a_table),
    path('contacts', views.contacts),
    path('gallery', views.gallery)
]
