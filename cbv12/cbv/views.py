from django.shortcuts import render
from django.views.generic import (
		View,
		ListView,
		CreateView,
		UpdateView,
		DeleteView,
		DetailView,
		TemplateView,
	)
from django.core.urlresolvers import reverse_lazy
from .models import Product
from .resources import ProductResource
from django.http import HttpResponse
# Create your views here.

class IndexView(View):

	def get(self,request):

		products = Product.objects.all()

		context= {
			"objects":products,
		}

		return render(request,'cbv/product_list.html',context)

class ProductListView(ListView):

	model = Product

class ProductDetailView(DetailView):

	model = Product

class ProductCreateView(CreateView):

	model = Product

	fields = ("name",'price','category','description')

	success_url = reverse_lazy("product-list")

class ProductDeleteView(DeleteView):

	model = Product
	
	success_url = reverse_lazy("product-list")

class ProductUpdateView(UpdateView):

	model = Product

	fields = ("name",'price','category','description')

	def get_success_url(self):
		product_id = self.kwargs['pk']
		return reverse_lazy('product-detail', kwargs={'pk': product_id})

def product_export_csv(request):

	product_resource = ProductResource()

	dataset = product_resource.export()

	response = HttpResponse(dataset.csv,content_type='text/csv')

	response['Content-Disposition'] = 'attachement; filename="product.csv"'

	return response

def product_export_json(request):

	product_resource = ProductResource()

	dataset = product_resource.export()

	response = HttpResponse(dataset.json,content_type='text/json')

	response['Content-Disposition'] = 'attachement; filename="product.json"'

	return response
