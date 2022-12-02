from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def select_view(request):
    context = {}
    print("Laduje")
    context["dataset"] = Users.objects.all()
    print("zaladowane")
    return render(request,"templates/base_view.html",context)