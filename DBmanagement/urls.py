from django.contrib import admin
from django.urls import path
from DBmanagement import views
urlpatterns = [

    path('cars/', views.cars_view), # works fine
    path('createcar/', views.car_create_view),# works fine
    path('deletecar/', views.car_delete_view), # works
    path('services/', views.services_view),# works
    path('servicesdelete/', views.service_delete_view), # no need for that but works
    path('createservice/', views.service_create_view),#works
    path('updateservice/', views.service_update_view), #works
    path('users/', views.users_view), #users
    #path('neworder/', views.new_order_view), # no use rent car is creating order
    path('orders/', views.order_view),# works
  #  path('orders/<id>/delete', views.order_delete_view),# no use
    path('servicestypes/', views.service_list_view), # design problem od database no use caue od table Services
    path('login/', views.login_view), # works
    path('staff/', views.staff_view), # works
    path('countorders/', views.orders_count),# works
    path('countuserorders/', views.user_orders_count), #works
    path('generatedashboard/', views.dashborad_view), #works
    path('clientupdate/', views.client_update_view), # works
    path('customerorders/', views.get_customer_orders), #works
    path('rentcar/', views.rent_car), #works
    path('returncar/', views.return_car),#works
    path('sendfeedback/', views.send_feedback), #works
    path('getuserrented/', views.get_user_rented_cars), # dont work due to database error
]