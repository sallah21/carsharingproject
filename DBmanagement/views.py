from django.http import JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *


# Create your views here.

def cars_view(request):
    context = {}
    print("Laduje")
    context["dataset"] = Cars.objects.all()
    print(Cars.objects.all())
    print("zaladowane")
    return render(request, "cars_view.html", context)


def users_view(request):
    context = {}
    print("Laduje")
    context["dataset"] = Staff.objects.all()
    print(Staff.objects.all())
    print("zaladowane")


    return render(request, "users_view.html", context)


def user_create_view(request):
    context = {}
    print("działa 1")
    print("działa 2")
    form = UserForm(request.POST or None)
    print("działa 3")
    if form.is_valid():
        form.save()

    context["form"] = form
    print("działa 4")
    return render(request, "createUser_view.html", context)
