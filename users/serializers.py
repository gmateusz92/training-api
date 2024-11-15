from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = User
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        user = User(**validated_data)  # Tworzenie instancji użytkownika
        user.set_password(validated_data['password'])  # Ustawienie hasła
        user.save()  # Zapisanie użytkownika w bazie danych
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(email=username, password=password)
            if not user:
                raise serializers.ValidationError(_("Invalid username or password."))
        else:
            raise serializers.ValidationError(_("Invalid username or password."))

        data["user"] = user
        return data

class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(min_length=8, write_only=True)

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()