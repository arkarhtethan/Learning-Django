from django.conf.urls import url
from .views import (
	index_page,
	laptop_list_page,
	desktop_list_page,
	desktop_add_page,
	laptop_add_page,
	laptop_delete_page,
	desktop_delete_page
	)


urlpatterns = [

	url(r'^$',index_page,name='index_view'),

	url(r'^desktop-list/',desktop_list_page,name='desktop_list'),
	url(r'^laptop-list/',laptop_list_page,name='laptop_list'),

	url(r'^add-desktop/',desktop_add_page,name='add_desktop'),
	url(r'^add-laptop/',laptop_add_page,name='add_laptop'),

	url(r'^delete-desktop/(?P<pk>\d+)/',desktop_delete_page,name='delete_desktop'),
	url(r'^delete-laptop/(?P<pk>\d+)/',laptop_delete_page,name='delete_laptop'),

	url(r'^update-desktop/(?P<pk>\d+)/',desktop_add_page,name='update_desktop'),
	url(r'^update-laptop/(?P<pk>\d+)/',laptop_add_page,name='update_laptop'),

]