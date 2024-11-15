from .models import User
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, ResetPasswordSerializer, ForgotPasswordSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.core.mail import send_mail
from django.urls import reverse

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(email=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ForgotPasswordView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            reset_url = request.build_absolute_uri(reverse('reset-password')) + f"?token={user.auth_token.key}"
            send_mail(
                'Reset your password',
                f'Click the link to reset your password: {reset_url}',
                'no-reply@example.com',
                [email],
                fail_silently=False,
            )
            return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Email not found"}, status=status.HTTP_404_NOT_FOUND)

class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data['token']
        new_password = serializer.validated_data['new_password']

        try:
            token_instance = Token.objects.get(key=token)
            user = token_instance.user

            user.set_password(new_password)
            user.save()

            return Response({"success": "Password has been reset."}, status=status.HTTP_200_OK)

        except Token.DoesNotExist:
            return Response({"error": "Invalid token."}, status=status.HTTP_400_BAD_REQUEST)
