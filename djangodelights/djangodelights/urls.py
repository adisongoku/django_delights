"""djangodelights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('inventory/', views.InventoryView.as_view(), name='inventory'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('purchase/', views.PurchaseView.as_view(), name='purchase'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('add_menu_item/', views.AddMenuItem.as_view(), name='add_menu_item'),
    path('add_ingredient/', views.AddIngredient.as_view(), name='add_ingredient'),
    path('add_recipe_requirements/', views.AddRecipeRequirements.as_view(), name='add_recipe_requirements'),
    path('add_new_purchase/', views.AddNewPurchase.as_view(), name='add_new_purchase'),
    path('inventory/<pk>/update_ingredient', views.UpdateIngredient.as_view(), name='update_ingredient')
]
