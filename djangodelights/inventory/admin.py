from ast import In
from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
# Register your models here.

@admin.site.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'unit', 'unit_price']

@admin.site.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']

@admin.site.register(RecipeRequirement)
class RecipeRequirementAdmin(admin.ModelAdmin):
    list_display = ['menu_item', 'ingredient', 'quantity']

@admin.site.register(Purchase)
class Purchase(admin.ModelAdmin):
    list_display = ['menut_item', 'timestamp']