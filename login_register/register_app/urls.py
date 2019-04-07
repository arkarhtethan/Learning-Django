from django.conf.urls import url
from .views import register_page
urlpatterns = [

	url(r'^$',register_page,name='register'),

]