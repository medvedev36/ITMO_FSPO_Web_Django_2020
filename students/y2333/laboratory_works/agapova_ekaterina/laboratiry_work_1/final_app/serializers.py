from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from final_app.models import Fabric, Product, Delivery, Sale
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'date_of_birth', 'card', 'email', 'first_name', 'last_name', 'is_superuser']


class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabric
        fields = ['id', 'address', 'name', 'country']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'name', 'vendor_code', 'fabric', 'image']


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'delivery_date', 'quantity', 'product', 'price_for_sale']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'date', 'quantity', 'user', 'delivery']


class StoreSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    fabric_name = serializers.CharField()
    fabric_country = serializers.CharField()
    price_for_sale = serializers.IntegerField()
    name = serializers.CharField()
    vendor_code = serializers.CharField()
    quantity = serializers.IntegerField()
    image = serializers.CharField()


class UserSalesSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    name = serializers.CharField()
    total = serializers.IntegerField()
    date = serializers.DateTimeField()

