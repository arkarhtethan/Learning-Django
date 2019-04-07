from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import RegisterForm
# Create your views here.

User = get_user_model()

def register_page(request):

	form = RegisterForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():

			username = form.cleaned_data.get('username')

			password = form.cleaned_data.get('password')
			
			email = form.cleaned_data.get('email')

			print(form.cleaned_data)

			User.objects.create_user(username=username,email=email,password=password)


	context = {

		'form': form,

	}

	return render(request,'register_app/register_page.html',context)
