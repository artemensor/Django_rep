from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from Vet.serializers import AnimalSerializer, DoctorSerializer, OrderSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Doctor, Order, Animal
import json
import random
from rest_framework import mixins
from rest_framework import generics
from django.template import loader
from rest_framework.reverse import reverse
from rest_framework import renderers


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class AnimalBlock(generics.GenericAPIView):
    queryset = Animal.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        animal = self.get_object()
        return Response('Name: {0}, Race: {1}'.format(animal.name, animal.get_race_display()))


# def index(request):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse("Home")

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'animals': reverse('animals-list', request=request, format=format),
        #'doctors': reverse('doctors-list', request=request, format=format),
        #'orders': reverse('orders-list', request=request, format=format),

    })


def createDoctor(request, name):
    doctor = Doctor(name= name, grade=str(random.randint(1,3)))
    doctor.save()
    return HttpResponse("{0} created".format(name))


def createAnimal(request, name):
    animal = Animal(name=name, race=str(random.randint(1, 4)))
    animal.save()
    return HttpResponse("{0} created".format(name))

def createOrder(request, name):
    animal = Animal(name=name, race=str(random.randint(1, 4)))
    animal.save()
    return HttpResponse("{0} created".format(name))

@api_view(['GET', 'POST'])
def showAnimals(request, format = None):

    # objects = Animal.objects.all()
    # template = loader.get_template('Vet/index.html')
    # context = {
    #     'animals': objects,
    # }
    # return render(request, 'Vet/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse(json.dumps(animals))
    if request.method == 'GET':
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #print(request.data)

        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def showAnimal(request, pk, format = None):

    try:
        animal = Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def showDoctors(request):
    objects = Doctor.objects.all()
    doctors = [j.name for j in objects]
    print(objects)
    print(doctors)
    return HttpResponse(json.dumps(doctors))


def showOrders(request):
    objects = Order.objects.all()
    orders = [(str(j.date), j.get_reason_display(), j.animal.name, j.doctor.name) for j in objects]
    print(objects)
    print(orders)
    return HttpResponse(json.dumps(orders))