from django.conf.urls import url
from .views import (
	IndexView,
	ProductListView,
	ProductDetailView,
	ProductDeleteView,
	ProductUpdateView,
	ProductCreateView,
	ProductTemplateView,
	)

urlpatterns = [

	url(r'^$',IndexView.as_view(),name="index_view"),
	url(r'^products/$',ProductListView.as_view(),name="product-list"),
	url(r'^products/template/$',ProductTemplateView.as_view(),name="product-template"),
	url(r'^products/create/$',ProductCreateView.as_view(),name="product-create"),
	url(r'^products/update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name="product-update"),
	url(r'^products/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name="product-delete"),
	url(r'^products/detail/(?P<pk>\d+)/$',ProductDetailView.as_view(),name="product-detail"),



]