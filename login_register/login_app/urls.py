from django.conf.urls import url

from .views import login_page

urlpatterns = [
	
	url(r'^$',login_page,name='login_page'),

]