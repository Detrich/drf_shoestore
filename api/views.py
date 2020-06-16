from django.shortcuts import render
from api.serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeTypeSerializer, ShoesSerializer
from shoeapp.models import Manufacturer,ShoeType,ShoeColor,Shoes
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeType.objects.all()

class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    queryset = ShoeColor.objects.all()

class ShoesViewSet(ModelViewSet):
    serializer_class = ShoesSerializer
    queryset = Shoes.objects.all()