from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from users.serializers import RegisterUserSerializer, UserSerializer

User = get_user_model()


class RegisterUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(created_at=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_at=self.request.user)

    def perform_update(self, serializer):
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner!')

        serializer.save()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
