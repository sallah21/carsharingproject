from django.contrib import admin
from django.urls import path
from DBmanagement import views
urlpatterns = [

    path('cars/', views.cars_view),
    path('users/', views.users_view),
    path('createuser/', views.user_create_view)
]