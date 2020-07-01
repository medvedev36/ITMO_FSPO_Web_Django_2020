from rest_framework import serializers

from .models import *


class BoardSerializers(serializers.ModelSerializer):
  # Сериализация доски

  class Meta:
    model = Board
    fields = ("id", "title")

class CardSerializers(serializers.ModelSerializer):
  # Сериализация Карточки

  class Meta:
    model = Card
    fields = ("id", "value", "index")

class PanelSerializers(serializers.ModelSerializer):
  # Сериализация Панели + карточки

  card = CardSerializers(many=True, read_only=True)

  class Meta:
    model = Panel
    fields = ("id", "title", "index", "card")
    depth = 1
