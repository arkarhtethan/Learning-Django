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

class IndexView(View):

	def get(self, request):

		context = {

			"object_list":Product.objects.all()

		}

		return render(request,'cbv/product_list.html',context)

class ProductTemplateView(TemplateView):

	template_name = 'cbv/product_list.html'

	def get_context_data(self, *args, **kwargs):

		data = super().get_context_data(*args, **kwargs)

		data['object_list'] = Product.objects.all()

		return data

class ProductListView(ListView):

	model = Product

class DrinkProductListView(ListView):

	model = Product

	def get_queryset(self):

		return Product.objects.drink()

class FoodProductListView(ListView):

	model = Product

	def get_queryset(self):

		return Product.objects.food()

class SnackProductListView(ListView):

	model = Product

	def get_queryset(self):

		return Product.objects.snack()

class NoodleProductListView(ListView):

	model = Product

	def get_queryset(self):

		return Product.objects.noodle()

class ProductDetailView(DetailView):

	model = Product

class ProductDeleteView(DeleteView):

	model = Product

	success_url = reverse_lazy("product-list")

class ProductUpdateView(UpdateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product-list")

class ProductCreateView(CreateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product-list")

















