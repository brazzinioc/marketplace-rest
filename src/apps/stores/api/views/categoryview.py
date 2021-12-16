from rest_framework import viewsets
from rest_framework.response import Response
from apps.stores.api.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.filter(status=True)
