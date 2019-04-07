from django.shortcuts import render
from .models import Desktop, Laptop
from .forms import DesktopForm, LaptopForm
# Create your views here.

laptops = Laptop.objects.all()
desktops = Desktop.objects.all()

def index_page(request,tag="desktop"):

	tag = tag.lower()

	if tag == 'desktop':

		return desktop_list_page(request)

	return laptop_list_page(request)

def desktop_list_page(request):

	return device_list_page(request,Desktop.objects.all(),'desktop')

def laptop_list_page(request):

	return device_list_page(request,Laptop.objects.all(),'laptop')

def device_list_page(request,devices=None,tag='desktop'):

	context = {

		"devices" : devices,

		"tag":tag.lower(),

	}

	return render(request,'crud_app/home_page.html',context)

def laptop_form_page(request,pk=None):

	cls = LaptopForm

	if pk:

		instance = Laptop.objects.get(pk=pk)

	else:

		instance = None

	return device_form_page(request,cls=cls,instance=instance,tag='Laptop')

def desktop_form_page(request,pk=None):

	cls = DesktopForm

	if pk:

		instance = Desktop.objects.get(pk=pk)

	else:

		instance = None

	return device_form_page(request,cls=cls,instance=instance,tag='Desktop')

def device_form_page(request,cls,tag,instance=None):

	if instance:

		form = cls(request.POST or None,instance=instance)

	else:

		form = cls(request.POST or None)		

	print(request.method)

	if request.method == "POST":

		print(request.POST)

		if form.is_valid():

			form.save()

			print(form.cleaned_data)

			print("Form is valid")

			return index_page(request,tag=tag)

	context = {

		"form" : form,

		"tag":tag,

	}

	return render(request,'crud_app/product_form.html',context)

def laptop_delete(request,pk=None):

	Laptop.objects.get(pk=pk).delete()

	return index_page(request,tag='laptop')

def desktop_delete(request,pk=None):

	Desktop.objects.get(pk=pk).delete()

	return index_page(request,tag='desktop')