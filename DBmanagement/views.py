import jwt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.utils import json

from .forms import *

@api_view(["POST"])

def login_view(request):
    try:
        username = request.data['username']
        password = request.data['password']
        print('ps ' + username + " " + password)
        print("searching in db")

        user = Staff.objects.filter(login=username, password=password).values() #get_object_or_404(Staff, login=username, password=password)()
        user = json.dumps(list(user), cls=DjangoJSONEncoder)
        print(user)
        print("Found")

        if user:
            print("payloading")
            payload = {
                'username': user[6],
                'password': user[7]
            }
            print("payloaded")
            token = jwt.encode(payload,"adrian")
            print("encoded")
            return JsonResponse({'token': token.decode('utf-8')}, status.HTTP_200_OK)
        else:
            return JsonResponse({'error': "did not found match"}, status.HTTP_401_UNAUTHORIZED)
    except KeyError:
        return JsonResponse({'error': "provide username and password"}, status.HTTP_400_BAD_REQUEST)

# Create your views here.
def users_view(request):
    context = {}
    queryset = Client.objects.all()
    data = serializers.serialize('json', queryset)
    context["dataset"] = queryset
    return JsonResponse(data, safe=False)


def users_create_view(request):
    context = {}
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = form
    return render(request, "createUser_view.html", context)

def user_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Staff, idstaff=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteservice_view.html", context)

def services_view(request):
    context = {}
    context["services"] = Service.objects.all()
    return JsonResponse(context)


def service_create_view(request):
    context = {}
    form = ServiceFrom(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "createService_view.html", context)

def service_list_view(request):
    context = {}
    queryset = Servicetype.objects.all()
    context["typesofservices"] = queryset
    data = serializers.serialize('json', queryset)
    context["dataset"] = queryset
    return JsonResponse(data, safe=False)
    return JsonResponse(context)


def service_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Service, idservice=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteservice_view.html", context)


def cars_view(request):
    context = {}
    queryset = Car.objects.all()
    context["dataset"] = queryset
    data = serializers.serialize('json', queryset)
    context["dataset"] = queryset
    return JsonResponse(data, safe=False)


def car_create_view(request):
    context = {}
    form = NewCarFrom(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "createcar_view.html", context)


def car_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Car, idcar=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deletecar_view.html", context)


def order_view(request):
    context = {}
    queryset = Order.objects.all()
    context["dataset"] = queryset
    data = serializers.serialize('json', queryset)
    context["dataset"] = queryset
    return JsonResponse(data, safe=False)

def new_order_view(request):
    context = {}
    form = NewOrderForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "createorder_view.html", context)


def order_delete_view(request):
    context = {}
    obj = get_object_or_404(Order, idorder=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteorder_view.html", context)


def staff_view(request):
    context = {}
    queryset = Staff.objects.all()
    data = serializers.serialize('json', queryset)
    context["dataset"] = queryset
    return JsonResponse(data, safe=False)