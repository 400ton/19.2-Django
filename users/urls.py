from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, email_verification, GeneratePasswordView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email.confirm/<str:verification_code>/', email_verification, name='email_verification'),
    path('reset-password/', GeneratePasswordView.as_view(template_name='users/reset_password.html'),
         name='reset_password')
]
