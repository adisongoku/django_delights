from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
# Register your models here.

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'unit', 'unit_price']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

@admin.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'ingredient', 'quantity']

@admin.register(Purchase)
class Purchase(admin.ModelAdmin):
    list_display = ['menu_item', 'timestamp']