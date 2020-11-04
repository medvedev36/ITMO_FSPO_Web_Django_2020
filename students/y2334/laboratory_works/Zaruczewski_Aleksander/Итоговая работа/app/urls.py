from django.contrib import admin
from django.urls import path, include

from app.views import *

urlpatterns = [
    path('accounts/register/', MyRegisterFormView.as_view(), name="signup_url"),
    path('accounts/logout/', logout, name="signup_url"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', start, name="start_url"),
    path('add_teacher', add_teacher, name="add_teacher_url"),
    path('add_lecture', add_lecture, name="add_lecture_url"),
    path('add_group', add_group, name="add_group_url"),
    path('add_subject', add_subject, name="add_subject_url"),
    path('add_lesson', add_lesson, name="add_lesson_url"),
    path('delete_lesson/<int:lesson_id>/', delete_lesson, name='delete_lesson_url'),
]