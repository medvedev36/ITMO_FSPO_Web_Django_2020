from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'price', 'pk']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'delta', 'time']
        read_only_fields = fields


class TripSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    transaction = TransactionSerializer()

    class Meta:
        model = Trip
        fields = ['car', 'time', 'transaction']
