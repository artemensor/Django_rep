from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.api_root), #path('', views.index, name='index'),
    path('doctors', views.showDoctors, name='showDoctors'),
    path('animals', views.AnimalList.as_view(), name = "animals-list"), #views.showAnimals, name='showAnimals'),
    path('animal/<int:pk>', views.AnimalDetail.as_view(), name = "animal-detail"), #views.showAnimal, name='showAnimal'),
    path('animal/<int:pk>/block/', views.AnimalBlock.as_view(), name='animal-block'),
    path('orders', views.showOrders, name='showOrders'),
    path('createDoctor/<str:name>/', views.createDoctor, name='createDoctor'),
    path('createAnimal/<str:name>', views.createAnimal, name='createAnimal'),
    #path('createOrder', views.showDoctors, name='showDoctors'),
]
urlpatterns = format_suffix_patterns(urlpatterns)