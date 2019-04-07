from django.conf.urls import url
from .views import (
		index_page,
		desktop_list_page,
		laptop_list_page,
		laptop_form_page,
		desktop_form_page,
		laptop_delete,
		desktop_delete,
	)
urlpatterns = [

	url(r'^$',index_page),

	url(r'^laptops/', laptop_list_page, name='laptops'),
	url(r'^desktops/', desktop_list_page, name='desktops'),

	url(r'^add-laptops/', laptop_form_page, name='add_laptop'),
	url(r'^add-desktops/', desktop_form_page, name='add_desktop'),

	url(r'delete-desktop/(?P<pk>\d+)/',desktop_delete,name="delete_desktop"),
	url(r'delete-laptop/(?P<pk>\d+)/',laptop_delete,name="delete_laptop"),
	
	url(r'update-laptop/(?P<pk>\d+)/',laptop_form_page,name="update_laptop"),
	url(r'update-desktop/(?P<pk>\d+)/',desktop_form_page,name="update_desktop"),
]