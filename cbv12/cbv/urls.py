from django.conf.urls import url
from .views import (
		IndexView,
		ProductListView,
		ProductDetailView,
		ProductCreateView,
		ProductUpdateView,
		ProductDeleteView,
		product_export_csv,
		product_export_json
	)

urlpatterns = [

	url(r'^products/$',ProductListView.as_view(),name='product-list'),
	
	url(r'^products/create/$',ProductCreateView.as_view(),name='product-create'),
	
	url(r'^products/export/csv/$',product_export_csv,name='product-export-csv'),

	url(r'^products/export/json/$',product_export_json,name='product-export-json'),
	
	url(r'^products/update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name='product-update'),
	
	url(r'^products/detail/(?P<pk>\d+)/$',ProductDetailView.as_view(),name='product-detail'),

	url(r'^products/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name='product-delete'),

]