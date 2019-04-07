from django.conf.urls import url
from .views import (
		IndexView,
		ProductListView,
		ProductCreateView,
		ProductDetailView,
		ProductDeleteView,
		ProductUpdateView,
		ProductTemplateView,
	)

urlpatterns = [

	url(r'^$',IndexView.as_view(),name='index_view'),

	url(r'^product-list/$',ProductListView.as_view(),name='product-list'),

	url(r'^product-template/$',ProductTemplateView.as_view(),name='product-template'),

	url(r'^product-create/$',ProductCreateView.as_view(),name='product-create'),

	url(r'^product-detail/(?P<pk>\d+)/$',ProductDetailView.as_view(),name='product-detail'),

	url(r'^product-delete/(?P<pk>\d+)/$',ProductDeleteView.as_view(),name='product-delete'),

	url(r'^product-update/(?P<pk>\d+)/$',ProductUpdateView.as_view(),name='product-update'),

]