from django.urls import path,re_path
from .views import test_view, greet_view,greet_view_with_param,user_sign_up_view,activate

app_name = 'email_app'

urlpatterns = [
	path('',test_view,name="index"),
	path('greet/',greet_view,name="greet"),
	path('register/',user_sign_up_view,name="register"),
	path('greet/<str:name>/',greet_view_with_param,name="greet-with-param"),
	path('activate/<str:uidb64>/<str:token>/',activate, name='activate'),
]




