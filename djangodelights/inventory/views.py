from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum
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

        return context


