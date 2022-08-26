from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    available_quantity = models.IntegerField(max_length=20, default=0, on_delete=models.CASCADE)
    price_per_unit = models.FloatField(max_length=20, default=0.0, on_delete=models.CASCADE)


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=20, default=0.0, on_delete=models.CASCADE)
    
