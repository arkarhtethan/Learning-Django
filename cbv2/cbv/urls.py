from django.conf.urls import url
from .views import (ProductListView,ProductDetailView,ProductCreateView,ProductDeleteView,ProductUpdateView)

urlpatterns = [

	url(r'^$',ProductListView.as_view(),name="product_list"),
	
	url(r'^products/detail/(?P<pk>\d+)/$',ProductDetailView.as_view(),name="product_detail"),
	
	url(r'^products/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name="product_delete"),
	
	url(r'^products/update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name="product_update"),
	
	url(r'^products/create/$',ProductCreateView.as_view(),name="product_create"),

]