from rest_framework import serializers
from apps.stores.models import Category, Store, StoreLocation, StoreLegalDetail, StoreSubPage, StoreSocialNetwork

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class StoreLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreLocation
        fields = "__all__"

class StoreLegaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreLegalDetail
        fields = "__all__"

class StoreSubPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreSubPage
        fields = "__all__"

class StoreSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreSocialNetwork
        fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)
    storelocation = StoreLocationSerializer(many=False, read_only=True)
    storesubpage = StoreSubPageSerializer(many=False, read_only=True)
    storelegaldetail = StoreLegaDetailSerializer(many=False, read_only=True)
    storesocialnetwork = StoreSocialNetworkSerializer(many=False, read_only=True)

    class Meta:
        model = Store
        fields = '__all__'
