from rest_framework import serializers
from apps.stores.models import Category, Store

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class StoreSerializer(serializers.Serializer):
    class Meta:
        model = Store
        fields = "__all__"
