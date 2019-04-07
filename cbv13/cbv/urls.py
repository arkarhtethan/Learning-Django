from .views import (
		ProductListView,
		ProductCreateView,
		ProductUpdateView,
		ProductDeleteView,
	)
from django.conf.urls import url

urlpatterns = [

	url(r'^$',ProductListView.as_view(),name="product-list"),
	url(r'^create/$',ProductCreateView.as_view(),name="product-create"),
	url(r'^update/$',ProductUpdateView.as_view(),name="product-update"),

]