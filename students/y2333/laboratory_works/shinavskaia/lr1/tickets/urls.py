from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('find_ticket/', views.ride_list, name='ride-list'),
    path('buy_ticket/<int:ride>/', views.buy_ticket, name='buy-ticket'),
    path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='ticket-info'),
    path('ticket/<int:pk>/delete', views.TicketDeleteView.as_view(), name='ticket-delete'),
    path('ticket/', views.ticket_list, name='ticket-list'),
]

