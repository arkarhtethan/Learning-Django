from django.conf.urls import url
from .views import (
	IndexView,
	ProductListView,
	ProductTemplateView,
	ProductDetailView,
	ProductCreateView,
	ProductUpdateView,
	ProductDeleteView
	)

urlpatterns = [

	url(r'^$',IndexView.as_view(),name="index_view"),
	url(r'^products/$',ProductListView.as_view(),name="product_list"),
	url(r'^products/create/$',ProductCreateView.as_view(),name="product_create"),
	url(r'^products/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name="product_delete"),
	url(r'^products/update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name="product_update"),
	url(r'^products/template/$',ProductTemplateView.as_view(),name="product_template_list"),
	url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view(),name="product_detail"),
]