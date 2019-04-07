from django.shortcuts import render
from django.views.generic import (ListView,DetailView,TemplateView,CreateView,DeleteView,UpdateView)
from .models import Product
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class TemplateViewTest(TemplateView):

	template_name = 'cbv_app/hello.html'

class ProductListView(ListView):

	model = Product

class ProductDetailView(DetailView):

	model = Product

class ProductCreate(CreateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("index_view")


class ProductUpdate(UpdateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("index_view")	

class ProductDeleteView(DeleteView):

	model = Product

	success_url = reverse_lazy("index_view")
