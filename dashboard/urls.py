from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from dashboard.views import dashboard
from user.forms import LoginForm
from user.views import CustomLoginView, ResetPasswordView, ChangePasswordView, RegisterView, profile

urlpatterns = [
    path('', dashboard, name='dashboard')
]
