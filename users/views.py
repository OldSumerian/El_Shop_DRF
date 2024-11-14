from django.contrib.auth.hashers import make_password

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ViewSet):
    """
    ViewSet для работы с моделью User
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserCreateAPIView(CreateAPIView):
    """
    API для создания нового пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """
        Сохраняем пароль в зашифрованном виде
        """
        serializer.save(password=make_password(serializer.validated_data["password"]))
