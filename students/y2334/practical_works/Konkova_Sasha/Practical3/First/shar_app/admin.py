from django.contrib import admin
from .models import Owner, Auto, Drive_docs, Owns, User

from django.contrib.auth.admin import UserAdmin
from .forms import User_CreationForm, User_ChangeForm

class User_Admin(UserAdmin):
    add_form = User_CreationForm
    form = User_ChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password', 'nationality', 'address')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

admin.site.register(User, User_Admin)
admin.site.register(Owner)
admin.site.register(Auto)
admin.site.register(Drive_docs)
admin.site.register(Owns)