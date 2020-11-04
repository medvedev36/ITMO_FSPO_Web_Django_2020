from django.urls import path
from .views import *

urlpatterns = [
    path('', prods_all, name="prod_list-url"),
    path('addProd/', addProd, name="add_prod-url"),
    path('addComp/', addComp, name="add_comp-url"),
    path('addMackler/', addMackler, name="add_mack-url"),
    path('editProdName/<int:id>/', editProdName),
    path('editProdCost/<int:id>/', editProdCost),
    path('editCompany/<int:id>', editCompany),
    path('editMack/<int:id>', editMackler),
    path('delete/<int:id>/', delete),
    ]