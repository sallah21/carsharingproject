import math

from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions, serializers
from DBmanagement.models import Client, Car, Order



class client_serializer(ModelSerializer):
    def update(self, instance, validated_data):
        print(self.context)
        #instance.name = self.context['Name']
        instance.name = validated_data.get('Name', instance.name)
        instance.surname = validated_data.get('Surmame', instance.surname)
        instance.phonenumber = validated_data.get('PhoneNumber', instance.phonenumber)
        instance.pesel = validated_data.get('Pesel', instance.pesel)

        instance.save()
        return instance
    class Meta:
        model = Client
        fields = "__all__"

class car_serializer(ModelSerializer):
    def create(self, validated_data):
        instance =  Car()
        instance.model = validated_data.get('Model', instance.model)
        instance.enginetype = validated_data.get('EngineType', instance.enginetype)
        instance.enginecapacity = validated_data.get('EngineCapacity', instance.enginecapacity)
        instance.status = validated_data.get('Status', instance.status)
        instance.numberofseats = validated_data.get('NumberOfSeats', instance.numberofseats)
        instance.value = validated_data.get('Value', instance.value)
        instance.save()
        return instance
    def update(self, instance, validated_data):
        instance.model = validated_data.get('Model', instance.model)
        instance.enginetype = validated_data.get('EngineType', instance.enginetype)
        instance.enginecapacity = validated_data.get('EngineCapacity', instance.enginecapacity)
        instance.status = validated_data.get('Status', instance.status)
        instance.numberofseats = validated_data.get('NumberOfSeats', instance.numberofseats)
        instance.value = validated_data.get('Value', instance.value)
        instance.save()
        return instance

    class Meta:
        model = Car
        fields = "__all__"