from rest_framework.serializers import ModelSerializer, StringRelatedField

from shoeapp.models import Shoes,ShoeColor,ShoeType,Manufacturer

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        basename='M'
        fields = ('name','website')

class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        basename="ST"
        fields = ('style',)

class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        basename="SC"
        fields = ('color_name',)

class ShoesSerializer(ModelSerializer):
    manufacturer = StringRelatedField()
    color = StringRelatedField()
    shoe_type = StringRelatedField()
    class Meta:
        model = Shoes
        basename="S"
        fields = ('size',
                  'brand',
                  'name',
                  'manufacturer',
                  'color',
                  'material',
                  'shoe_type',
                  'fasten_type'
                  )
