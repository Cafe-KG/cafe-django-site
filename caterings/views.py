from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from caterings.models import Catering, BookCatering
from caterings.serializers import CateringSerializer, BookCateringSerializer


class CateringViewSet(ModelViewSet):
    queryset = Catering.objects.all()
    serializer_class = CateringSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookCateringViewSet(ModelViewSet):
    queryset = BookCatering.objects.all()
    serializer_class = BookCateringSerializer
    permission_classes = [permissions.IsAuthenticated]
