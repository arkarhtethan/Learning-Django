from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import (login, authenticate)
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


def login_view(request):

	form = LoginForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():

			username = form.cleaned_data.get('username')

			password = form.cleaned_data.get('password')

			print(username)

			print(password)

			user = authenticate(username=username, password=password)

			print(user)

			if user is not None:

				print("User logged in")

				login(request, user)

				print(user.is_authenticated())

				print()

				return HttpResponseRedirect(reverse("auth:login-success"))

	context = {

		"form": form,

		"submit_button_name": "LogIn",

		"header": "LogIn",

	}

	return render(request,"login_register/authentication_form.html",context)

def login_success(request):

	return render(request,'login_register/login_success.html')

def register_view(request):

	form = RegisterForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():

			username = form.cleaned_data.get('username')
			
			email = form.cleaned_data.get('email')

			password = form.cleaned_data.get('password1')

			user_obj = User.objects.get_or_create(username=username, email=email, password=password)

			print(user_obj)



	context = {

		"form": form,

		"submit_button_name": "Register",

		"header": "Register",

	}

	return render(request,"login_register/authentication_form.html",context)