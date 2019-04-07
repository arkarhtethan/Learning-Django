from .models import Product
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.

class IndexView(View):

	def get(self,request):

		return HttpResponse("Hello From View class")

class ProductTemplateView(TemplateView):

	template_name = 'cbv/product_list.html'

	def get_context_data(self,*args,**kwargs):

		context_data = super().get_context_data(*args,**kwargs)

		context_data['object_list'] = Product.objects.all()

		return context_data

class ProductListView(ListView):

	model = Product

class ProductDetailView(DetailView):

	model = Product


class ProductCreateView(CreateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):

	model = Product

	fields = "__all__"

	success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):

	model = Product

	success_url = reverse_lazy("product_list")
