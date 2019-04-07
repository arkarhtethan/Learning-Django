from django.urls import path
from .views import register_view, activate_account_view

app_name = "email_app"

urlpatterns = [
    path('register/', register_view, name="register"),
    path('activate/<str:uidb64>/<str:token>/', activate_account_view, name="activate"),
]