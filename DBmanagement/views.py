import jwt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.utils import json

from .forms import *

@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    try:
        username = request.data['username']
        password = request.data['password']
        print('ps ' + username + " " + password)
        print("searching in db")

        user = Staff.objects.filter(login=username, password=password).values().first() #get_object_or_404(Staff, login=username, password=password)()

        print(user)
        print("Found")

        if user:
            print("payloading")
            payload = {
                'idStaff': user['idstaff'],
            }
            print("payloaded")
            token = jwt.encode(payload,"adrian")
            print("encoded")
            return JsonResponse({'token': token.decode('utf-8')})
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

            context = {}
            queryset = Client.objects.all()
            data = serializers.serialize('json', queryset)
            context["dataset"] = queryset
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
    context = {}
    queryset = Servicetype.objects.all()
    context["typesofservices"] = queryset
    data = serializers.serialize('json', queryset)
    context["dataset"] = queryset
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
def car_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Car, idcar=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deletecar_view.html", context)


@api_view(["GET"])
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
            queryset = Order.object.all().count()
            print(queryset)
            data = serializers.serialize('json', queryset)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "authentication error" })
    except KeyError:
        return JsonResponse({'error': "database error"})

@api_view(["GET"])
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