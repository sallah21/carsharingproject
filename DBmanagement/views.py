from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import *


# Create your views here.
def users_view(request):
    context = {}
    print("Laduje")
    context["dataset"] = Client.objects.all()
    print(Client.objects.all())
    print("zaladowane")
    return render(request, "users_view.html", context)


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
    print("Laduje")
    context["services"] = Service.objects.all()
    print(context["services"][0].price)
    print("zaladowane")
    return render(request, "users_view.html", context)


def service_create_view(request):
    context = {}
    print("działa 1")
    print("działa 2")
    form = ServiceFrom(request.POST or None)
    print("działa 3")
    if form.is_valid():
        form.save()

    context["form"] = form
    print("działa 4")
    return render(request, "createService_view.html", context)

def service_list_view(request):
    context = {}
    context["typesofservices"] = Servicetype.objects.all()
    return render(request, "users_view.html", context)


def service_delete_view(request, id):
    context = {}
    obj = get_object_or_404(Service, idservice=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "deleteservice_view.html", context)


def cars_view(request):
    context = {}
    print("Laduje")
    context["dataset"] = Car.objects.all()
    print(Car.objects.all())
    print("zaladowane")
    return render(request, "cars_view.html", context)


def car_create_view(request):
    context = {}
    form = NewCarFrom(request.POST or None)
    print("działa 3")
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
    print("Laduje")
    context["dataset"] = Order.objects.all()
    print(Order.objects.all())
    print(context["dataset"][0].idorder)
    print("zaladowane")
    return render(request, "orders_view.html", context)
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