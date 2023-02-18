import datetime
import random

import shortuuid
from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions, serializers
from DBmanagement.models import Client, Car, Order, Listofcars, Service


class listofcar_serializer(ModelSerializer):
    def create(self, validated_data):
        instance = Listofcars()
        instance.idlistofcars = random.randint(1000, 9999)
        instance.idorder = validated_data.get('idOrder')
        instance.idcar= validated_data.get('idCar')
        instance.save()
        return  instance
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

    def update(self, instance, validated_data):
        instance.dateoforder = validated_data.get('DateOfOrder', instance.dateoforder)
        instance.datestart = validated_data.get('DateStart', instance.datestart)
        instance.dateend = validated_data.get('DateEnd', instance.dateend)
        instance.zipcode = validated_data.get('ZipCode', instance.zipcode)
        instance.city = validated_data.get('City', instance.city)
        instance.street = validated_data.get('Street', instance.street)
        instance.buldingnumber = validated_data.get('BuildingNumber', instance.buldingnumber)
        instance.feedback = validated_data.get('Feedback', instance.feedback)
        instance.idclient = validated_data.get('idClient', instance.idclient)
        instance.save()
        return instance
    class Meta:
        model = Order
        fields = "__all__"


class client_serializer(ModelSerializer):
    def update(self, instance, validated_data):
        print(self.context)
        #instance.name = self.context['Name']
        instance.name = validated_data.get('Name', instance.name)
        instance.surname = validated_data.get('Surname', instance.surname)
        instance.phonenumber = validated_data.get('PhoneNumber', instance.phonenumber)
        instance.pesel = validated_data.get('Pesel', instance.pesel)
        instance.save()
        return instance
    class Meta:
        model = Client
        fields = "__all__"

class car_serializer(ModelSerializer):
    def create(self, validated_data):
        instance = Car()
        instance.idcar =  random.randint(1000, 9999)
        instance.model = validated_data.get('model', instance.model)
        instance.enginetype = validated_data.get('enginetype', instance.enginetype)
        instance.enginecapacity = validated_data.get('enginecapacity', instance.enginecapacity)
        instance.status = validated_data.get('status', instance.status)
        instance.numberofseats = validated_data.get('numberofseats', instance.numberofseats)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance
    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.enginetype = validated_data.get('enginetype', instance.enginetype)
        instance.enginecapacity = validated_data.get('enginecapacity', instance.enginecapacity)
        instance.status = validated_data.get('status', instance.status)
        instance.numberofseats = validated_data.get('numberofseats', instance.numberofseats)
        instance.value = validated_data.get('value', instance.value)
        instance.save()
        return instance

    class Meta:
        model = Car
        fields = "__all__"

class service_serializer(ModelSerializer):
        def create(self, validated_data):
            instance = Service()
            instance.idservice = random.randint(1000, 9999)
            instance.dateservicestart = datetime.date.today()
            instance.dateserviceend = None
            instance.price = None
            instance.idcar =Car.objects.get(idcar=validated_data.get('idcar', instance.idcar))
            instance.save()
            return instance
        def update(self, instance,validated_data):

            instance.dateservicestart = validated_data.get('dateservicestart', instance.dateservicestart)
            instance.dateserviceend = validated_data.get('dateserviceend', instance.dateserviceend)
            instance.price = validated_data.get('price', instance.price)
            instance.idcar = validated_data.get('idcar', instance.idcar)
            instance.save()
            return instance
        class Meta:
            model = Service
            fields = "__all__"