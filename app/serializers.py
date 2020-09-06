from rest_framework import serializers

from .models import *
from django.utils.timezone import now
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"
    def create(self,validated_data):
        return State.objects.create(**validated_data)
    def update(self,instance,validated_data):

        instance.state = validated_data.get('state',instance.state)

        instance.save()
        return instance

class RequestTypeSerializer(serializers.ModelSerializer):
    requesttype = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = RequestType
        fields = "__all__"
    def create(self,validated_data):
        return RequestType.objects.create(**validated_data)
    def update(self,instance,validated_data):

        instance.requesttype = validated_data.get('requesttype',instance.requesttype)

        instance.save()
        return instance
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
    def create(self,validated_data):
        return Status.objects.create(**validated_data)
    def update(self,instance,validated_data):

        instance.status = validated_data.get('status',instance.status)

        instance.save()
        return instance

class NewRequestSerializer(serializers.ModelSerializer):
    requesttype = serializers.PrimaryKeyRelatedField(many=True,queryset=RequestType.objects.all())
    #state = StateSerializer()
    #status = StatusSerializer()
    class Meta:
        model = RequestList
        fields = ["user","requesttype","requestdesc","city","state","pincode","countrycode","phone_number","status","created_at"]
    #def create(self,validated_data):
    #    return RequestList.objects.create(**validated_data)
    #def update(self,instance,validated_data):
    #    instance.user = validated_data.get('user',instance.user)
    #    instance.requesttype = validated_data.get('requesttype',instance.requesttype)
    #    instance.requestdesc = validated_data.get('requestdesc',instance.requestdesc)
    #    instance.city = validated_data.get('city', instance.city)
    #    instance.state = validated_data.get('state', instance.state)
    #    instance.pincode = validated_data.get('pincode', instance.pincode)
    #    instance.countrycode = validated_data.get('countrycode', instance.countrycode)
    #    instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #    instance.save()
    #    return instance

class UpdateRequestSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    class Meta:
        model = RequestList
        fields = ["status","remarks","updated_by","updated_at"]
    def update(self,instance,validated_data):
        instance.status = validated_data.get('status',instance.status)
        instance.remarks  = validated_data.get('remarks',instance.remarks)
        instance.updated_by = validated_data.get('updated_by',instance.updated_by)
        instance.updated_at == validated_data.get("updated_at",now)
        instance.save()
        return instance