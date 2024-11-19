from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя
    """
    class Meta:
        model = User
        fields = "__all__"

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Сериализатор для получения токена JWT
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['password'] = user.password

        return token
