from rest_framework import serializers

from tour_buro.models import Bus, Excursion_route,Crew_member,Completed_trip


class manySerializers(serializers.ListSerializer):

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        obj_mapping = {obj.id: obj for obj in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for obj_id, data in data_mapping.items():
            obj = obj_mapping.get(obj_id, None)
            if obj is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(obj, data))

        # Perform deletions.
        for obj_id, obj in obj_mapping.items():
            if obj_id not in data_mapping:
                obj.delete()

        return ret


class BusSerializers(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Bus
        fields = '__all__'
        list_serializer_class = manySerializers


class Excursion_RouteSerializers(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Excursion_route
        fields = '__all__'
        list_serializer_class = manySerializers

class Crew_memberSerializers(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Crew_member
        fields = '__all__'
        list_serializer_class = manySerializers

class Completed_tripSerializers(serializers.ModelSerializer):

    id = serializers.IntegerField()

    class Meta:
        model = Completed_trip
        fields = '__all__'
        list_serializer_class = manySerializers