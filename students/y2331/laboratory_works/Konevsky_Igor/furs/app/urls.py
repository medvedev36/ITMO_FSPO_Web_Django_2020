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
    path('coat_list/', views.coatlist),
    path('profile/', views.purchaselist),
    path('farm_form/', login_required(FarmCreate.as_view(success_url='/farm_list/'))),
    path('fur_form/', login_required(FurCreate.as_view(success_url='/fur_list/'))),
    path('coat_form/', login_required(CoatCreate.as_view(success_url='/coat_list/'))),
    path('coat_buy/<int:pk>', login_required(views.buy)),
    path('farm_update/<int:pk>', login_required(FarmUpdate.as_view())),
    path('fur_update/<int:pk>', login_required(FurUpdate.as_view())),
    path('coat_update/<int:pk>', login_required(CoatUpdate.as_view())),
    path('farm_delete/<int:pk>', login_required(views.farmdelete)),
    path('fur_delete/<int:pk>', login_required(views.furdelete)),
    path('coat_delete/<int:pk>', login_required(views.coatdelete)),
    path('purchase_delete/<int:pk>', login_required(views.purchasedelete)),
    path('review_form/<int:pk>', views.addreview),
    path('reviews/<int:pk>', views.reviewlist),
]
