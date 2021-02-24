from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors', views.showDoctors, name='showDoctors'),
    path('animals', views.showAnimals, name='showAnimals'),
    path('orders', views.showOrders, name='showOrders'),
    path('createDoctor/<str:name>/', views.createDoctor, name='createDoctor'),
    path('createAnimal/<str:name>', views.createAnimal, name='createAnimal'),
    #path('createOrder', views.showDoctors, name='showDoctors'),
]