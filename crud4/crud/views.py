from django.shortcuts import render,get_object_or_404,redirect
from .models import Product

from .forms import ProductForm
# Create your views here.

def product_list(request):

	context = {

		"object_list":Product.objects.all(),

	}

	return render(request,"crud/product_list.html",context)

def product_detail(request, id):
	object_ = get_object_or_404(Product, pk=id)

	context = {

			"object":object_,

		}

	return render(request,"crud/product_detail.html",context)

def product_create(request):

	form = ProductForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():

			form.save()

			return redirect("crud:product-list")

	context = {

		"form": form,

	}

	return render(request,"crud/product_form.html",context)

def product_update(request,id):

	instance = get_object_or_404(Product,pk=id)

	form = ProductForm(request.POST or None,instance=instance)

	if request.method == "POST":

		if form.is_valid():

			form.save()

			return redirect("crud:product-list")

	context = {

		"form": form,

	}

	return render(request,"crud/product_form.html",context)

def product_delete(request, id):
	
	Product.objects.get(pk=id).delete();

	return redirect("crud:product-list")
