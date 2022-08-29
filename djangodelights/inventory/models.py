from django.db import models

# Create your models here.

class Ingredient(models.Model):
    KILOGRAM = 'KG'
    GRAM = 'G'
    POUND = "LB"
    OUNCE = "OZ"

    WEIGHT_UNITS = (
        (KILOGRAM, "Kilogram"),
        (GRAM, "Gram"),
        (POUND, "Pound"),
        (OUNCE, "Ounce"),
    )

    name = models.CharField(max_length=255)
    quantity = models.IntegerField(max_length=20, default=0)
    unit = models.CharField(max_length=20, choices=WEIGHT_UNITS, default=GRAM)
    punit_price = models.FloatField(max_length=20, default=0.0)
        

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(max_length=20, default=0.0)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=20, default=0.0)

     
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
