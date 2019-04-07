from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .forms import LoginForm
# Create your views here.

def login_page(request):

	form = LoginForm(request.POST or None)

	if request.method == "POST":

		print("request.user.is_authenticated()  ",request.user.is_authenticated())

		if form.is_valid():

			username = form.cleaned_data.get('username')

			password = form.cleaned_data.get('password')

			user = authenticate(username=username, password=password)

			if user is not None:

				login(request, user)

				print(form.cleaned_data)

				print("User logged in")

				print("request.user.is_authenticated()  ",request.user.is_authenticated())


	context = {

		'form': form,

	}

	return render(request,'login_app/login_page.html',context)
