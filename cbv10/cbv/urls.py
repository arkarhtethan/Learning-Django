from django.conf.urls import url
from .views import (
		ProductView,
		ProductListView,
		ProductDetailView,
		ProductDeleteView,
		ProductUpdateView,
		ProductCreateView,
		ProductTemplateView,
	)

urlpatterns = [
	url(r'^$',ProductView.as_view(),name='product-view'),
	url(r'^proudcts/$',ProductListView.as_view(),name='product-list'),
	url(r'^proudcts/template/$',ProductTemplateView.as_view(),name='product-template'),
	url(r'^proudcts/create/$',ProductCreateView.as_view(),name='product-create'),
	url(r'^proudcts/delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name='product-delete'),
	url(r'^proudcts/detail/(?P<pk>\d+)/$',ProductDetailView.as_view(),name='product-detail'),
	url(r'^proudcts/update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name='product-update'),
]