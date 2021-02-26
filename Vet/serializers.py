from rest_framework import serializers
from Vet.models import Animal, Doctor, Order


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    block = serializers.HyperlinkedIdentityField(view_name='animal-block', format='html')

    class Meta:
        model = Animal
        fields = ["url", "block", 'id', 'name', 'race', 'creation_date', 'gender']



class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='doctor-highlight', format='html')

    class Meta:
        model = Doctor
        fields = ["url", "link",'id', 'name', 'grade']



class OrderSerializer(serializers.HyperlinkedModelSerializer):
    link = serializers.HyperlinkedIdentityField(view_name='order-highlight', format='html')

    class Meta:
        model = Order
        fields = ["url", "link",'id', 'animal', 'doctor', 'reason', 'date']