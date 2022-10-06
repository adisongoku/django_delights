from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum, F
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
import datetime
# Create your views here.

class HomeView(TemplateView):
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

class InventoryView(ListView):
    model = Ingredient

class MenuItemView(ListView):
    model = MenuItem


class RecipeRequirementView(ListView):
    model = RecipeRequirement

class PurchaseView(ListView):
    model = Purchase

class ReportView(TemplateView):
    template_name = 'inventory/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['purchases'] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(revenue=Sum('menu_item__price'))['revenue']
        context['revenue'] = revenue
        costs = 0
        for purchase in Purchase.objects.all():
            for recipe_requirement in purchase.menu_item.reciperequirement_set.all():
                costs += recipe_requirement.ingredient.unit_price * \
                    recipe_requirement.quantity


        context['costs'] = costs
        context['profit'] = revenue - costs

        return context


class AddMenuItem(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/add_menu_item.html'


class AddIngredient(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/add_ingredient.html'

class AddRecipeRequirements(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementsForm
    template_name = 'inventory/add_recipe_requirements.html'

class AddNewPurchase(CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/add_new_purchase.html'

class UpdateIngredient(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/update_ingredient.html'
