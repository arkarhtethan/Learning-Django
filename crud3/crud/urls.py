from django.conf.urls import url
from .views import (
	
	index_page,

	desktop_list,

	laptop_list,

	laptop_form,

	desktop_form,

	delete_desktop,

	delete_laptop,

	)

urlpatterns = [

	url(r'^$',index_page,name='index_page'),
	
	url(r'^desktop-list/$',desktop_list,name='desktop_list'),
	url(r'^laptop-list/$',laptop_list,name='laptop_list'),

	url(r'^create-desktop/$',desktop_form,name='create_desktop'),
	url(r'^create-laptop/$',laptop_form,name='create_laptop'),

	url(r'^create-desktop/(?P<pk>\d+)/$',desktop_form,name='update_desktop'),
	url(r'^create-laptop/(?P<pk>\d+)/$',laptop_form,name='update_laptop'),

	url(r'^delete-desktop/(?P<pk>\d+)/$',delete_desktop,name='delete_desktop'),
	url(r'^delete-laptop/(?P<pk>\d+)/$',delete_laptop,name='delete_laptop'),

]