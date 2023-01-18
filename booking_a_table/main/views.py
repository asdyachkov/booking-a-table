import django_filters
from django.db.models import Q
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Salats, SideDishesAndSoups, HotDishes, Drinks, PhotoLinks, RentATable
from .forms import RentATableForm
from .serializers import SalatsSerializer


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


class SalatsViewSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'items_per_page'
    max_page_size = 1000


class SalatsViewSet(viewsets.ModelViewSet):
    filterset_fields = ['weight', 'cost']
    queryset = Salats.objects.all()
    serializer_class = SalatsSerializer
    pagination_class = SalatsViewSetPagination

    @action(methods=['post'], detail=True)
    def salat(self, request, pk=None):
        serializer = SalatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': serializer.data})
        else:
            return Response({'status': 'Invalid data'})

    @action(methods=['get'], detail=False)
    def photos(self, request):
        photos = PhotoLinks.objects.all()
        return Response({'photos': [item.link for item in photos]})

    @action(methods=['get'], detail=True)
    def qrent(self, request, pk=None):
        rents = RentATable.objects.filter(Q(client_name__startswith=pk) | Q(phone_number__icontains=pk))
        return Response({'rents': [(rent.client_name, rent.phone_number) for rent in rents]})

    @action(methods=['get'], detail=False)
    def salatswithphoto(self, request):
        salats = Salats.objects.filter(photo__isnull=True)
        return Response({'photos': [item.title for item in salats]})



# class SalatsApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Salats.objects.all()
#     serializer_class = SalatsSerializer
#
#
# class SalatsApiList(generics.ListAPIView):
#     serializer_class = SalatsSerializer
#     pagination_class = SalatsViewSetPagination
#
#     def get(self, request):
#         user = self.request.user
#         salats = Salats.objects.filter(purchaser=user)
#         return Response({'salats': SalatsSerializer(salats, many=True).data})
#
#
# class SalatsApiUpdate(generics.UpdateAPIView):
#     queryset = Salats.objects.all()
#     serializer_class = SalatsSerializer

# class SalatsAPIView(generics.ListAPIView):
#     def get(self, request):
#         salats = Salats.objects.all()
#         return Response({'salats': SalatsSerializer(salats, many=True).data})
#
#     def post(self, request):
#         serializer = SalatsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'salat': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed"})
#
#         try:
#             instance = Salats.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesnt exist"})
#         serializer = SalatsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE is not allowed"})
#
#         try:
#             instance = Salats.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object doesnt exist"})
#
#         instance.delete()
#
#         return Response({"salat": "delet post " + str(pk)})


