from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
		View,
		ListView,
		CreateView,
		UpdateView,
		DeleteView,
		DetailView,	
		TemplateView,
	)
# Create your views here.


class IndexView(View):

	def get(self,request):

		return HttpResponse("Hello World")

class ProductListView(ListView):

	model = Product

class ProductDetailView(DetailView):

	model = Product

class ProductTemplateView(TemplateView):

	template_name = 'cbv/product_list.html'

	def get_context_data(self,*args,**kwargs):

		context_data = super().get_context_data(*args,**kwargs)

		context_data['object_list'] = Product.objects.all()

		return context_data

class ProductDeleteView(DeleteView):

	model = Product

	success_url = reverse_lazy("product_list")

class ProductCreateView(CreateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product_list")	
