from django.urls import path
from .views import UserCreateView, validate_username

app_name ='ajax'

urlpatterns = [

	path('sign-up/',UserCreateView.as_view(),name="signup"),
	path('ajax/validate-username/',validate_username,name="validate-username"),

]