from django.urls import path
from .views import register_view, activate_view

app_name="email_app"

# http://{{ domain }}{% url 'email:activate' uidb64=uid token=token %}

urlpatterns = [
	
	path('register/',register_view,name="register"),
	path('activate/<str:uidb64>/<str:token>/',activate_view,name="activate"),

]