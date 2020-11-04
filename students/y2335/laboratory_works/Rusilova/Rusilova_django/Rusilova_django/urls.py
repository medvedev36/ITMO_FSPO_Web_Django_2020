
from django.conf.urls import url
from django.urls import path, include
from fur_shop import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('purchase_delete/<int:pk>', views.deletePurchase, name = 'purchase_delete'),
    path('review_delete/<int:pk>', views.deleteReview, name = 'review_delete'),
    path('reviews/<int:pk>', views.ReviewList, name = 'reviews'),
    path('review/<int:pk>', login_required(views.addReview), name = 'review'),
    path('profile/', views.PurchaseView, name = 'profile'),
    path('fur_buy/<int:pk>', login_required(views.buy),name='fur_buy'),
    url(r"^furlist/",views.FurList.as_view(), name="fur_list"),
    url(r"^home/", views.HomePageView.as_view() ,name="home"),
    path('farmlist/', views.FarmList, name = 'farm_list'),
    path('accounts/', include('django.contrib.auth.urls', ),name='login'),
    path('register/', views.RegisterView.as_view(), name = 'register'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    url(r"^farmform/",login_required(views.FarmCreateView.as_view()), name="farm_create"),
    url(r"^furform/",login_required(views.FurCreateView.as_view()), name="fur_create")
]
