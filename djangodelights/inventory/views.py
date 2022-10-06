from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from django.db.models import Sum, F
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'inventory/signup.html'

def logout_request(request):
    logout(request)
    return redirect('home')


class HomeView(TemplateView):
    template_name = 'inventory/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

@login_required
class InventoryView(LoginRequiredMixin, ListView):
    model = Ingredient

class MenuItemView(LoginRequiredMixin, ListView):
    model = MenuItem


class RecipeRequirementView(LoginRequiredMixin, ListView):
    model = RecipeRequirement

class PurchaseView(LoginRequiredMixin, ListView):
    model = Purchase

class ReportView(LoginRequiredMixin, TemplateView):
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


class AddMenuItem(LoginRequiredMixin, CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'inventory/add_menu_item.html'


class AddIngredient(LoginRequiredMixin, CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/add_ingredient.html'

class AddRecipeRequirements(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementsForm
    template_name = 'inventory/add_recipe_requirements.html'

class AddNewPurchase(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'inventory/add_new_purchase.html'

class UpdateIngredient(LoginRequiredMixin, UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'inventory/update_ingredient.html'
