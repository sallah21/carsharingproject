import datetime
import random

import shortuuid
from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions, serializers
from DBmanagement.models import Client, Car, Order

class order_serializer(ModelSerializer):
    def create(self, validated_data):
        instance = Order()
        instance.idorder= random.randint(1000, 9999)
        print("UUID: ", instance.idorder )
        instance.dateoforder = datetime.date.today()
        if validated_data.get('DateStart') <= str(datetime.date.today()):
            print("Start:", validated_data.get('DateStart'))
            print("Today : ", str(datetime.date.today()))
            raise Exception("Date of start before date of order")
        instance.datestart = validated_data.get('DateStart', instance.datestart)

        if validated_data.get('DateStart') > validated_data.get('DateEnd'):
            print("Start:", validated_data.get('DateStart'))
            print("End: ", validated_data.get('DateEnd'))
            raise Exception("Date of start after date of end")
        instance.dateend = validated_data.get('DateEnd', instance.dateend)
        instance.zipcode = validated_data.get('ZipCode', instance.zipcode)
        instance.city = validated_data.get('City', instance.city)
        instance.street = validated_data.get('Street', instance.street)
        instance.buldingnumber = validated_data.get('BuildingNumber', instance.buldingnumber)
        instance.feedback = validated_data.get('Feedback', instance.feedback)
        instance.idclient = Client.objects.get(idclient=validated_data.get('idClient', instance.feedback))
        instance.save()
        return instance

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