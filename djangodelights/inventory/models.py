from django.db import models

# Create your models here.

class Ingredient(models.Model):
    KILOGRAM = "KG"
    GRAM = "G"
    POUND = "LB"
    OUNCE = "OZ"
    LITER = "L"
    MILILITER = "ML"
    PIECE = "P"

    WEIGHT_UNITS = (
        (KILOGRAM, "Kilogram"),
        (GRAM, "Gram"),
        (POUND, "Pound"),
        (OUNCE, "Ounce"),
        (LITER, "Liter"),
        (MILILITER, "Mililiter"),
        (PIECE, 'Piece')
    )

    name = models.CharField(max_length=255)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=20, choices=WEIGHT_UNITS, default=GRAM)
    unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
        

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.title


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

     
class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
