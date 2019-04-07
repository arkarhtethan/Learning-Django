from .models import Product
from django.shortcuts import render
from django.views.generic import (
	View,
	TemplateView,
	ListView,
	DetailView,
	UpdateView,
	DeleteView,
	CreateView
	)
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class IndexView(View):

	def get(self, request):

		object_list = Product.objects.all()

		context = {

			"object_list": object_list,

		}

		return render(request,'cbv/product-list.html',context)

class ProductTemplateView(TemplateView):

	template_name = 'cbv/product-list.html'

	def get_context_data(self, *args, **kwargs):

		context_data = super().get_context_data(*args, **kwargs)

		context_data['object_list'] = Product.objects.all()

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

	success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy('product-list')
