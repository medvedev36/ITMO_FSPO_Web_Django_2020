from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import *


class User_groups_serial(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class Owner_registration_serial(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'phone', 'password', 'email', 'groups',
                  'user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')

    def save(self):
        new_owner = CustomUser(
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            patronymic=self.validated_data['patronymic'],
        )
        password = self.validated_data['password']
        new_owner.set_password(password)
        owner_group = Group.objects.get(name='Auto_owners')
        new_owner.save()
        owner_group.user_set.add(new_owner)

    # def validate...


class Brands_for_workshops_serial(serializers.ModelSerializer):
    class Meta:
        model = Served_brands
        fields = ('brand',)


class Workshops_serial(serializers.ModelSerializer):
    brands = Brands_for_workshops_serial(many=True)

    class Meta:
        model = Workshop
        fields = ('number', 'address', 'brands')


class Autos_for_owner_serial(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ('id', 'number', 'brand', 'model', 'year', 'tech_passport')


class Workshops_for_application_serial(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = ('id', 'number', 'address')


class Applications_for_owner_serial(serializers.ModelSerializer):
    auto = Autos_for_owner_serial()
    workshop = Workshops_for_application_serial()

    class Meta:
        model = Application
        fields = ('id', 'auto', 'workshop', 'date', 'date_init', 'status', 'description')


class Application_serial(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'auto', 'workshop', 'date', 'date_init', 'status', 'description')

    def get_auto(self, obj):
        return self.initial_data['auto']

    def get_workshop(self, obj):
        return self.initial_data['workshop']

    def validate(self, data):
        if Served_brands.objects.filter(workshop=data['workshop'].id,
                                        brand=(Auto.objects.get(id=data['auto'].id)).brand):
            return data
        raise serializers.ValidationError("Cannot be served")
