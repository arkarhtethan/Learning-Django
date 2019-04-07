from .views import (
		ProductView,
		ProductListView,
		ProductDetailView,
		ProductDeleteView,
		ProductUpdateView,
		ProductCreateView,
		ProductTemplateView,
	)
from django.conf.urls import url

urlpatterns = [
	url(r'^$',ProductView.as_view(),name='prodct-index'),
	url(r'^products/$',ProductListView.as_view(),name='product-list'),
	url(r'^products/template/$',ProductTemplateView.as_view(),name='product-template'),
	url(r'^products/create/$',ProductCreateView.as_view(),name='product-create'),
	url(r'^products/detail/(?P<pk>\d+)/$',ProductDetailView.as_view(),name='product-detail'),
	url(r'^products/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name='product-delete'),
	url(r'^roducts/update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name='product-update'),
]