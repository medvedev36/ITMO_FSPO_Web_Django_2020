from django.contrib.auth.decorators import login_required
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('farm_list/', views.farmlist, ),
    path('fur_list/', views.furlist),
    path('buyer_list/', views.buyerlist),
    path('purchase_list/', views.purchaselist),
    path('farm_form/', login_required(FarmCreate.as_view(success_url='/farm_list/'))),
    path('fur_form/', login_required(FurCreate.as_view(success_url='/fur_list/'))),
    path('buyer_form/', login_required(BuyerCreate.as_view(success_url='/buyer_list/'))),
    path('purchase_form/', login_required(PurchaseCreate.as_view(success_url='/purchase_list/'))),
    path('farm_update/<int:pk>', login_required(FarmUpdate.as_view())),
    path('fur_update/<int:pk>', login_required(FurUpdate.as_view())),
    path('buyer_update/<int:pk>', login_required(BuyerUpdate.as_view())),
    path('purchase_update/<int:pk>', login_required(PurchaseUpdate.as_view())),
    path('farm_delete/<int:pk>', login_required(views.farmdelete)),
    path('fur_delete/<int:pk>', login_required(views.furdelete)),
    path('buyer_delete/<int:pk>', login_required(views.buyerdelete)),
    path('purchase_delete/<int:pk>', login_required(views.purchasedelete)),
]
