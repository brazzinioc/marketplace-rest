from rest_framework import serializers
from apps.cities.models import City, State, Colony


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class ColonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Colony
        fields = "__all__"
