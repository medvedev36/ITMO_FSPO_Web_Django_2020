from rest_framework import serializers
from autoApp.models import *

class Models_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Car_Models
        fields = ("id", "model_name", )

class Autoshops_Serializers(serializers.ModelSerializer):
    car_models = Models_Serializers(many=True)
    class Meta:
        model = Autoshops
        fields = ("id", "shop_name", "address", "car_models")

class Masters_Serializers(serializers.ModelSerializer):
    shop_number = Autoshops_Serializers()
    class Meta:
        model = Masters
        fields = ("id", "full_name_m", "phone_number", "shop_number")

class Custumer_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ("id", "full_name_c", "address_c", "phone_number_c", "passport")

class Cars_Serializers(serializers.ModelSerializer):
    costumer_id = Custumer_Serializers()
    model_id = Models_Serializers()
    class Meta:
        model = Cars
        fields = ("state_number", "year_of_issue", "date_sheet_number", "model_id", "costumer_id")

class Cars_Post_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = "__all__"

class Comrepair_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Comprehensive_Repair
        fields = ("id",)

class Works_Serializers(serializers.ModelSerializer):
    shop_number_w = Autoshops_Serializers()
    master_id = Masters_Serializers()
    comrepair_id = Comrepair_Serializers()
    class Meta:
        model = Completed_Works
        fields = ("id", "type_of_repair", "receipt_date", "repair_completion_date", "repair_cost", "shop_number_w", "state_number_w", "master_id", "comrepair_id")

class Works_Post_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Completed_Works
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.type_of_repair = validated_data.get('type_of_repair', instance.type_of_repair)
        instance.repair_completion_date = validated_data.get('repair_completion_date', instance.repair_completion_date)
        instance.repair_cost = validated_data.get('repair_cost', instance.repair_cost)
        instance.shop_number_w = validated_data.get('shop_number_w', instance.shop_number_w)
        instance.state_number_w = validated_data.get('state_number_w', instance.state_number_w)
        instance.master_id = validated_data.get('master_id', instance.master_id)
        instance.comrepair_id = validated_data.get('comrepair_id', instance.comrepair_id)
        instance.save()
        return instance

class Comrepair_Post_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Comprehensive_Repair
        fields = "__all__"
