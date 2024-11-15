from django.urls import path

from .views import (ForgotPasswordView, LoginView, RegisterView,
                    ResetPasswordView, UpdateUserView)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("update-user/", UpdateUserView.as_view(), name="update-user"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
]
