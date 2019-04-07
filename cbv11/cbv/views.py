from .models import Product
from django.shortcuts import render
from django.views.generic import (
		View,
		ListView,
		DetailView,
		DeleteView,
		UpdateView,
		CreateView,
		TemplateView,
	)
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def get_all_product_list():

	return Product.objects.all()

class ProductView(View):

	def get(self,request):

		context = {

			"object_list": get_all_product_list()

		}

		return render(request,'cbv/product_list.html',context)

class ProductListView(ListView):

	model = Product

class ProductDetailView(DetailView):

	model = Product

class ProductDeleteView(DeleteView):

	model = Product

	success_url = reverse_lazy("product-list")

class ProductCreateView(CreateView):

	model = Product

	fields = "__all__"

class ProductUpdateView(UpdateView):
	
	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product-list")

class ProductTemplateView(TemplateView):

	template_name = 'cbv/product_list.html'

	def get_queryset(self,*args, **kwargs):

		return get_all_product_list()
