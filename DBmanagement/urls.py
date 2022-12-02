from django.contrib import admin
from django.urls import path
from DBmanagement import views
urlpatterns = [

    path('test/', views.select_view),

]