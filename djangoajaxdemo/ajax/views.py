from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
# Create your views here.

class UserCreateView(CreateView):

	template_name = "ajax/sign_up.html"

	form_class = UserCreationForm

def validate_username(request):

	username = request.GET.get("username", None)

	if username is not None:

		data = {
			"is_taken":User.objects.filter(username__iexact=username).exists()
		}

	return JsonResponse(data)


