from django.shortcuts import render
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
    context["dataset"] = Users.objects.all()
    return render(request, "users_view.html", context)


def user_create_view(request):
    context = {}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "createUser_view.html",context)
