from django.http import HttpResponse
from .models import Doctor, Order, Animal
import json
import random
from django.template import loader


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse("Home")

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


def showAnimals(request):

    objects = Animal.objects.all()
    #animals = [j.name for j in objects]
    print(objects)
    #print(animals)
    context = {}
    template = loader.get_template('Vet/index.html')
    context = {
        'animals': objects,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(json.dumps(animals))

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