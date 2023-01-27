import datetime

import jwt
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .forms import *
from DBmanagement.serializers import client_serializer, car_serializer, order_serializer


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = Staff.objects.filter(login=username, password=password).values().first() #get_object_or_404(Staff, login=username, password=password)()

        if user:
            payload = {
                'idStaff': user['idstaff'],
            }
            token = jwt.encode(payload,"adrian")
            return JsonResponse({
                'token': token.decode('utf-8'),
                'iduser': user['idstaff']
            })
        else:
            return JsonResponse({'error': "did not found match"}, status.HTTP_401_UNAUTHORIZED)
    except KeyError:
        return JsonResponse({'error': "provide username and password"}, status.HTTP_400_BAD_REQUEST)

# Create your views here
@api_view(["GET"])
@permission_classes([AllowAny])
def users_view(request):
    id =jwt.decode( request.data['token'], "adrian")
    print(id)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Client.objects.all()
            data = serializers.serialize('json', queryset)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "authentication error" })
    except KeyError:
        return JsonResponse({'error': "database error"} )


@api_view(["POST"])
def users_create_view(request):
    context = {}
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = form
    return render(request, "createUser_view.html", context)


@api_view(["POST"])
def user_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Staff, idstaff=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteservice_view.html", context)

@api_view(["POST"])
@permission_classes([AllowAny])
def client_update_view(request):
    id = jwt.decode(request.data['token'], "adrian")

    userid = request.data['idClient']
    print(id)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Client.objects.get(idclient = userid)
            print('Q: ', queryset)
            cs = client_serializer()
            data = client_serializer.update(self=cs,instance=queryset, validated_data=request.data)
            return Response(status=status.HTTP_200_OK)
    except KeyError:
        return JsonResponse({'error': KeyError})

@api_view(["GET"])
@permission_classes([AllowAny])
def services_view(request):
    id = jwt.decode(request.data['token'], "adrian")
    print(id)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Service.objects.all()
            data = serializers.serialize('json', queryset)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "authentication error" })
    except KeyError:
        return JsonResponse({'error': "database error"} )


@api_view(["POST"])
def service_create_view(request):
    context = {}
    form = ServiceFrom(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "createService_view.html", context)


@api_view(["GET"])
def service_list_view(request):
    queryset = Servicetype.objects.all()
    data = serializers.serialize('json', queryset)
    return JsonResponse(data, safe=False)
    return JsonResponse(context)


@api_view(["POST"])
def service_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Service, idservice=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteservice_view.html", context)

@api_view(["GET"])
@permission_classes([AllowAny])
def cars_view(request):
    id = jwt.decode(request.data['token'], "adrian")
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Car.objects.all()
            data = serializers.serialize('json', queryset)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "authentication error"})
    except KeyError:
        return JsonResponse({'error': "database error"})


@api_view(["POST"])
def car_create_view(request):
    context = {}
    form = NewCarFrom(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "createcar_view.html", context)

@api_view(["POST"])
@permission_classes([AllowAny])
def car_update_view(request):
    id = jwt.decode(request.data['token'], "adrian")

    carid = request.data['idCar']
    print(id)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Car.objects.get(idCar=carid)
            print('Q: ', queryset)
            cs = car_serializer()
            data = car_serializer.update(self=cs, instance=queryset, validated_data=request.data)
    except KeyError:
        return JsonResponse({'error': KeyError})

@api_view(["POST"])
@permission_classes([AllowAny])
def rent_car(request):
    id = jwt.decode(request.data['token'], "adrian")

    carid = request.data['idCar']
    print(id)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Car.objects.get(idcar=carid)
            print('Q: ', queryset)

            if queryset.status == 'rented':
                return Response({"error": "Car is rented"}, status=status.HTTP_409_CONFLICT)
            os = order_serializer()
            cs = car_serializer()
            print("creating")
            os.create(request.data)
            print("updating")
            car_serializer.update(cs, instance=queryset, validated_data={'Status': 'rented'})
            return Response(status=status.HTTP_201_CREATED)

    except KeyError:
            return JsonResponse({'error': KeyError})

@api_view(["POST"])
@permission_classes([AllowAny])
def return_car(request):
    id = jwt.decode(request.data['token'], "adrian")
    carid = request.data['idCar']
    print(id)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Car.objects.get(idcar=carid)
            print('Q: ', queryset)
            if queryset.status == 'free':
                return Response({"error": "Car is free"}, status=status.HTTP_409_CONFLICT)

            cs = car_serializer()
            print("updating")
            car_serializer.update(cs, instance=queryset, validated_data={'Status': 'free'})
            return Response(status=status.HTTP_201_CREATED)

    except KeyError:
            return JsonResponse({'error': KeyError})

@api_view(["POST"])
def car_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Car, idcar=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deletecar_view.html", context)

@api_view(["GET"])
@permission_classes([AllowAny])
def get_customer_orders(request):
    id = jwt.decode(request.data['token'], "adrian")

    userid = request.data['idUser']
    print(id)
    print(userid)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Order.objects.get(idclient=userid)
            print('Q: ', queryset)
            data = serializers.serialize('json', [queryset])
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "authentication error"}, status = status.HTTP_401_UNAUTHORIZED)
    except KeyError:
        return JsonResponse({'error': KeyError})



@api_view(["GET"])
@permission_classes([AllowAny])
def order_view(request):
    id = jwt.decode(request.data['token'], "adrian")
    print(id)
    try:
        if Staff.objects.get(idStaff=id['idStaff']):
            queryset = Order.objects.all()
            data = serializers.serialize('json', queryset)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "authentication error" })
    except KeyError:
        return JsonResponse({'error': "database error"} )


@api_view(["POST"])
def new_order_view(request):
    context = {}
    form = NewOrderForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "createorder_view.html", context)


@api_view(["POST"])
def order_delete_view(request):
    context = {}
    obj = get_object_or_404(Order, idorder=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteorder_view.html", context)


@api_view(["GET"])
@permission_classes([AllowAny])
def orders_count(request):
    id = jwt.decode(request.data['token'], "adrian")
    print(id)
    try:
        if Staff.objects.get(idstaff=id['idStaff']):
            queryset = Order.objects.all().count()
            print(queryset)
            return JsonResponse({"number_of_orders": queryset}, safe=False)
        else:
            return JsonResponse({"error": "authentication error" })
    except KeyError:
        return JsonResponse({'error': "database error"})


@api_view(["GET"])
@permission_classes([AllowAny])
def staff_view(request):
    id = jwt.decode(request.data['token'], "adrian")
    print(id)
    try:
        if Staff.objects.get(idStaff= id["idStaff"]):
            queryset = Staff.objects.all()
            data = serializers.serialize('json', queryset)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "authentication error" })
    except KeyError:
        return JsonResponse({'error': "database error"} )


@api_view(["GET"])
@permission_classes([AllowAny])
def dashborad_view(request):
    id = jwt.decode(request.data['token'], "adrian")
    userid = 1
    print(id)
    try:
        if Staff.objects.get(idstaff= id['idStaff']):
            user = Client.objects.filter(idclient=userid).values().first()
            payment = 0
            try:
                for o in Order.objects.filter(idclient=userid):
                    p = Payment.objects.filter(idorder=o.idorder).first()
                    payment = payment + p.amounttopay - p.amountpayed

            except KeyError:
                print("error", KeyError)
                return JsonResponse({"error": "server error"})

            return JsonResponse({
                'name': user['name'],
                'surname': user['surname'],
                'phonenumber': user['phonenumber'],
                'topay': payment
            })
        else:
            return JsonResponse({"error": "authientication error"})
    except KeyError:
        return JsonResponse({'error': KeyError, })