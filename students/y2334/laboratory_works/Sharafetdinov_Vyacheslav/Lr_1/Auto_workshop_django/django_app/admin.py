from django.contrib import admin
from .models import *
from .forms import *


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = (
        (None, {'fields': ('username', 'phone', 'email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'patronymic')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('number', 'address')


class ServedBrandsAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'brand')


class AutoAdmin(admin.ModelAdmin):
    list_display = ('owner', 'number', 'brand', 'model', 'year', 'tech_passport')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'autos', 'first_name', 'last_name', 'patronymic', 'phone')

    def autos(self, obj):
        return '\n'.join([auto.tech_passport for auto in obj.autos.all()])


class WorkAdmin(admin.ModelAdmin):
    list_display = ('employee', 'auto', 'date_beg', 'date_end', 'description', 'price')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('auto', 'workshop', 'date', 'date_init', 'status', 'description')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Served_brands, ServedBrandsAdmin)
admin.site.register(Auto, AutoAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Application, ApplicationAdmin)
