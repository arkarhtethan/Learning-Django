from django.shortcuts import render, redirect
from .models import Desktop, Laptop
from .forms import DesktopForm,LaptopForm
# Create your views here.

def index_page(request):

	return render(request,'crud_app/index.html')

def desktop_list_page(request):

	devices = Desktop.objects.all()

	context = {

		"devices" : devices,

		'tag' : "desktop"

	}

	return render(request,'crud_app/index.html',context)

def laptop_list_page(request):

	devices = Laptop.objects.all()

	context = {

		"devices" : devices,

		'tag' : "laptop"

	}

	return render(request,'crud_app/index.html',context)

def desktop_add_page(request,pk=None):

	if pk:

		instance = Desktop.objects.get(pk=pk)

		form = DesktopForm(request.POST or None, instance=instance)

	else:

		form = DesktopForm(request.POST or None)		

	if request.method == "POST":

		if form.is_valid():

			print(form.cleaned_data)

			form.save()

			return redirect("desktop_list")

	context = {

		"form": form,

		"tag" : "Desktop"

	}

	return render(request,'crud_app/product_form.html',context)

def laptop_add_page(request,pk=None):

	if pk:

		instance = Laptop.objects.get(pk=pk)

		form = LaptopForm(request.POST or None, instance=instance)

	else:

		form = LaptopForm(request.POST or None)		

	if request.method == "POST":

		if form.is_valid():

			print(form.cleaned_data)

			form.save()

			return redirect("laptop_list")

	context = {

		"form": form,

		"tag" : "Laptop"

	}

	return render(request,'crud_app/product_form.html',context)

def desktop_delete_page(reqeust,pk=None):

	Desktop.objects.get(pk=pk).delete()

	return redirect("desktop_list")

def laptop_delete_page(request,pk=None):

	Laptop.objects.get(pk=pk).delete()

	return redirect("laptop_list")
