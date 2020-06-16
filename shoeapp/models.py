from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ShoeType(models.Model):
    style = models.CharField(max_length=30)
    def __str__(self):
        return self.style

class ShoeColor(models.Model):
    RED = 'Red'
    ORANGE = 'Orange'
    GREEN = 'Green'
    BLUE = 'Blue'
    INDIGO = 'Indigo'
    VIOLET = 'Violet'
    WHITE = 'White'
    BLACK = 'Black'
    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black')
    ]
    color_name = models.CharField(max_length=10,choices=COLOR_CHOICES,default=BLACK)
    def __str__(self):
        return self.color_name

class Shoes(models.Model):
    size = models.IntegerField(default=7)
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor,on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType,on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)
    def __str__(self):
        return self.name