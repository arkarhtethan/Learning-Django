from django.shortcuts import render
from django.views.generic import ( ListView,DetailView,CreateView,DeleteView,UpdateView )
from django.core.urlresolvers import reverse_lazy
from .models import Product
# Create your views here.

class ProductListView(ListView):

	model = Product

class ProductDetailView(DetailView):

	model = Product

class ProductCreateView(CreateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):

	model = Product

	success_url = reverse_lazy("product_list")

