from django.shortcuts import render,redirect
from .models import Desktop, Laptop
from .forms import DesktopForm, LaptopForm
# Create your views here.

def index_page(reqeust):

	return render(reqeust,"crud/home.html")

def desktop_list(reqeust):

	devices = Desktop.objects.all()

	context = {

		"devices" : devices,

		"tag" : "desktop",

	}

	return render(reqeust,"crud/home.html",context)

def laptop_list(reqeust):

	devices = Laptop.objects.all()

	context = {

		"devices" : devices,

		"tag" : "laptop",

	}

	return render(reqeust,"crud/home.html",context)

def laptop_form(reqeust,pk=None):

	if pk:

		instance = Laptop.objects.get(pk=pk)

		form = LaptopForm(reqeust.POST or None,instance=instance)

	else:

		form = LaptopForm(reqeust.POST or None)		

	if reqeust.method == "POST":

		if form.is_valid():

			form.save()

			return redirect("laptop_list")

	context = {

		"form":form,

		"tag":"Laptop",

	}

	return render(reqeust,"crud/form.html",context)

def desktop_form(reqeust,pk=None):

	if pk:

		instance = Desktop.objects.get(pk=pk)

		form = DesktopForm(reqeust.POST or None,instance=instance)
	
	else:

		form = DesktopForm(reqeust.POST or None)

	if reqeust.method == "POST":

		if form.is_valid():

			form.save()

			return redirect("desktop_list")

	context = {

		"form":form,

		"tag":"Desktop",

	}

	return render(reqeust,"crud/form.html",context)

def delete_desktop(reqeust,pk=None):

	if pk:

		Desktop.objects.get(pk=pk).delete()

		return redirect("desktop_list")

def delete_laptop(reqeust,pk=None):

	if pk:

		Laptop.objects.get(pk=pk).delete()

		return redirect("laptop_list")