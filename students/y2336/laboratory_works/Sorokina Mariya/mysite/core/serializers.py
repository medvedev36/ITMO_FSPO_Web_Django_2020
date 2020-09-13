from rest_framework import serializers

from .models import *

class AttractionTypeSerializers(serializers.ModelSerializer):
  # Сериализация типа аттракциона

  class Meta:
    model = AttractionType
    fields = ("id", "attraction_type")

class PlaygroundSerializers(serializers.ModelSerializer):
  # Сериализация площадки

  # attraction = AttractionSerializers(many=True, read_only=True)

  class Meta:
    model = Playground
    fields = ("id", "image", "address_playground", "last_name")
    # fields = ("id", "address_playground", "last_name", "attraction") // Если надо передавать еще и аттракционы для площадки

class AttractionSerializers(serializers.ModelSerializer):
  # Сериализация аттракциона

  type = AttractionTypeSerializers(read_only=True)

  class Meta:
    model = Attraction
    fields = ("id", "image", "name_attraction", "year_purchase", "adult_price", "children_price", "type")

class UseAttractionSerializers(serializers.ModelSerializer):
  # Сериализация информации об использовании аттракциона

  attraction = AttractionSerializers(read_only=True)
  playground = PlaygroundSerializers(read_only=True)

  class Meta:
    model = Use_attraction
    fields = ("id", "date", "adult_ticket", "children_ticket", "playground", "attraction")


class MyPurchaseSerializers(serializers.ModelSerializer):
  # Сериализация истории покупок пользователя

  attraction = AttractionSerializers(read_only=True)

  class Meta:
    model = My_purchase
    fields = ("id", "date", "price", "attraction")




