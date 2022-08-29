from curses.ascii import HT
from tkinter import Menu
from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
# Create your views here.


def list_inventory(request):
    inventory_list = Ingredient.objects.all()
    context = {'inventory_list': inventory_list}
    return render(request, 'inventory/inventory.html', context)

class InventoryView(ListView):
    model = Ingredient

class MenuItemView(ListView):
    model = MenuItem

class RecipeRequirementView(ListView):
    model = RecipeRequirement

class PurchaseView(ListView):
    model = ListView

    