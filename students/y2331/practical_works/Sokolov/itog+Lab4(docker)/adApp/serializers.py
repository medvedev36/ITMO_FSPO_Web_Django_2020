from rest_framework import serializers
from adApp.models import *

# Сериализация ТВ каналов
class Channel_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"

# Сериализация ТВ программ для метода get
class TVShow_Serializers(serializers.ModelSerializer):
    idChannel = Channel_Serializers()
    class Meta:
        model = TVShow
        fields = ("id", "time", "cost", "show_name", "idChannel")

# Сериализация ТВ программ для метода post
class AddTVShow_Serializers(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ("time", "cost", "show_name", "idChannel")

# Сериализация рекламных компаний для метода get
class Advertiser_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = "__all__"

# Сериализация рекламных роликов для метода get
class Advertising_Serializers(serializers.ModelSerializer):
    idAdvertiser = Advertiser_Serializers()
    class Meta:
        model = Advertising
        fields = ("id", "adName", "time", "idAdvertiser")

# Сериализация рекламных роликов для методов post и put
class AddAdvertising_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.adName = validated_data.get('adName', instance.adName)
        instance.time = validated_data.get('time', instance.time)
        instance.idAdvertiser = validated_data.get('idAdvertiser', instance.idAdvertiser)
        instance.save()
        return instance

# Сериализация поазов роликов для метода get
class AdBreak_Serializers(serializers.ModelSerializer):
    idTVShow = TVShow_Serializers()
    idAdvertising = Advertising_Serializers()
    class Meta:
        model = AdBreak
        fields = ("date", "idTVShow", "idAdvertising")

# Сериализация поазов роликов для метода post
class AddAdBreak_Serializers(serializers.ModelSerializer):
    class Meta:
        model = AdBreak
        fields = ("date", "idTVShow", "idAdvertising")
