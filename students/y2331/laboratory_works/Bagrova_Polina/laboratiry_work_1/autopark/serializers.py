from rest_framework import serializers

from autopark.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ("id", "username")


class ModelsSerializer(serializers.ModelSerializer):
    """Сериализация моделей автомобилей"""

    class Meta:
        model = Model_of_car
        fields = ("model", "brand")


class CarsSerializer(serializers.ModelSerializer):
    """Сериализация машин"""

    class Meta:
        model = Cars
        fields = ("license_plate", "model", "run")


class ClientsSerializer(serializers.ModelSerializer):
    """Сериализация клиентов"""

    class Meta:
        model = Clients
        fields = ("id", "name", "address")

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class DriversSerializer(serializers.ModelSerializer):
    """Сериализация водителя"""
    user = UserSerializer()

    class Meta:
        model = Drivers
        fields = ("last_name", "first_name", "category", "experience", "address", "birth_year", "user")


class DriverNameSerializer(serializers.ModelSerializer):
    """Сериализация имени водителя"""

    class Meta:
        model = Drivers
        fields = ("last_name", "first_name")


class ManifestsSerializer(serializers.ModelSerializer):
    """Сериализация путевых листов"""
    driver = DriverNameSerializer()

    class Meta:
        model = Manifests
        fields = ("id", "date", "driver", "car")

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.driver = validated_data.get('driver', instance.driver)
        instance.car = validated_data.get('car', instance.car)
        instance.save()
        return instance


class ManifestsPostSerializer(serializers.ModelSerializer):
    """Сериализация путевых листов для POST-запроса"""

    class Meta:
        model = Manifests
        fields = ("date", "car")


class OrdersSerializer(serializers.ModelSerializer):
    """Сериализация заказов"""

    class Meta:
        model = Orders
        fields = ("id", "client", "direction", "kilometrage", "weight", "price", "second_point", "manifest")

    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.direction = validated_data.get('direction', instance.direction)
        instance.kilometrage = validated_data.get('kilometrage', instance.kilometrage)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.price = validated_data.get('price', instance.price)
        instance.second_point = validated_data.get('second_point', instance.second_point)
        instance.manifest = validated_data.get('manifest', instance.manifest)
        instance.save()
        return instance


class ItemsSerializer(serializers.ModelSerializer):
    """Сериализация товаров"""

    class Meta:
        model = Items
        fields = ("name",)


class OrderCompositionSerializer(serializers.ModelSerializer):
    """Сериализация состава заказа"""
    item = ItemsSerializer()

    class Meta:
        model = Order_composition
        fields = ("item", "quantity")
