from django.conf.urls import url
from .views import (
	product_list,
	product_detail,
	product_create,
	product_update,
	product_delete,
	)
urlpatterns = [

	url(r'^products/$',product_list,name="product-list"),
	url(r'^products/create/$',product_create,name="create"),
	url(r'^products/update/(?P<id>\d+)/$',product_update,name="update"),
	url(r'^products/delete/(?P<id>\d+)/$',product_delete,name="delete"),
	url(r'^products/(?P<id>\d+)/$',product_detail,name="product-detail"),

]