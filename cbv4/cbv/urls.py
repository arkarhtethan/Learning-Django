from django.conf.urls import url
from .views import (
		IndexView,
		ProductTemplateView,
		ProductListView,
		ProductDetailView,
		ProductCreateView,
		ProductUpdateView,
		ProductDeleteView
	)

urlpatterns = [
	
	url(r'^index/$',IndexView.as_view(),name="index_view"),
	
	url(r'^products/$',ProductListView.as_view(),name="product_list"),
	
	url(r'^products/template/$',ProductTemplateView.as_view(),name="product_template"),
	
	url(r'^products/create/$',ProductCreateView.as_view(),name="product_create"),
	
	url(r'products/update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name="product_update"),

	url(r'products/detail/(?P<pk>\d+)/$',ProductDetailView.as_view(),name="product_detail"),
	
	url(r'products/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name="product_delete"),


]