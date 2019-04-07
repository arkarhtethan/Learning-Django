from django.shortcuts import render
from django.views.generic import (
		TemplateView,
		ListView,
		CreateView,
		UpdateView,
		DeleteView,

	)
from .models import Product
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class ProductListView(ListView):

	model = Product

class ProductCreateView(CreateView):

	model = Product

	success_url = reverse_lazy("product-list")

class ProductUpdateView(UpdateView):

	model = Product

	success_url = reverse_lazy("product-list")

class ProductDeleteView(DeleteView):

	model = Product

	success_url = reverse_lazy("product-list")
