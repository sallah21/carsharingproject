from django.contrib import admin
from django.urls import path
from DBmanagement import views
urlpatterns = [

    path('cars/', views.cars_view),
    path('createcar/', views.car_create_view),
    path('cars/<id>/delete', views.car_delete_view),
    path('services/', views.services_view),
    path('services/<id>/delete', views.service_delete_view),
    path('createservice/', views.service_create_view),
    path('users/', views.users_view),
    path('neworder/', views.new_order_view),
    path('orders/', views.order_view),
    path('orders/<id>/delete', views.order_delete_view),
    path('servicestypes/', views.service_list_view),
    path('login/', views.login_view),
    path('staff/', views.staff_view),
]