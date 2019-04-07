from django.conf.urls import url
from .views import (
	ProductListView,
	ProductDetailView,
	TemplateViewTest,
	ProductCreate,
	ProductUpdate,
	ProductDeleteView
	)

urlpatterns = [

	url(r'^$',ProductListView.as_view(),name='index_view'),

	url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view(),name='detail_view'),
	
	url(r'^products/update/(?P<pk>\d+)/$',ProductUpdate.as_view(),name='update_view'),
	url(r'^products/create/$',ProductCreate.as_view(),name='create_view'),
	
	url(r'^products/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name='delete_view'),



]