from rest_framework import viewsets
from rest_framework.response import Response
from apps.stores.api.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    #queryset = serializer_class.Meta.model.objects.filter(status=True)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(status=True).prefetch_related('categories') # Many to Many
        return self.get_serializer().Meta.model.objects.filter(pk=pk, status=True).first().select_related('categories', 'storelocation', 'storelegaldetail', 'storesubpage', 'storesocialnetwork')




