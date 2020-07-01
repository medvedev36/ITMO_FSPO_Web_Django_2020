# coding=utf-8
from  django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tour_list, name = "tour_list"),
    path('thanks/<int:pk>', views.thanks, name = "thanks"),
    path('remove/<int:pk>', views.remove, name="remove"),
    path('tour/<int:pk>', views.tour, name = "tour"),
    path('motorship_list/', views.motorship_list, name = "motorships"),
    path('sailor_list/', views.sailor_list, name = "sailors"),
    path("buy/<int:pk>", views.tour_buy, name = "tour_buy"),
    path("tickets/", views.tickets, name="tickets"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path("find/", views.find, name = "find")
]