from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', welcome, name='welcome'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('binding/', binding, name='binding'),
    path('participation/', participation, name='participation'),
    path('training/', training, name='training'),
    path('competitions_list/', competition_out, name='competitions_list'),
    path('trainers_list/', trainer_out, name='trainers_list'),
    path('sportsmen_list/', sportsman_out, name='sportsmen_list'),
    path('traumas_list/', trauma_out, name='traumas_list'),
    path('contest_list/', contest_out, name='contest_list'),
    path('workout_list/', workout_out, name='workout_list'),
    path('competitions_form/', competition_in.as_view(), name='competitions_form'),
    path('trainers_form/', trainer_in.as_view(), name='trainers_form'),
    path('sportsmen_form/', sportsman_in.as_view(), name='sportsmen_form'),
    path('traumas_form/', trauma_in.as_view(), name='traumas_form'),
    path('contest_form/', contest_in.as_view(), name='contest_form'),
]
