from .tokens import account_activation_token
from .forms import UserSingUpForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text

# Create your views here.

def user_sign_up_view(request):

	form = UserSingUpForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():
			
			user = form.save(commit=False)

			user.is_active = False

			user.save()

			current_site = get_current_site(request)

			mail_subject = 'Activate your shopping account.'

			message = render_to_string('activate_email_template.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token':account_activation_token.make_token(user),
			})

			print("REGISTER ",urlsafe_base64_encode(force_bytes(user.pk)))

			to_email = form.cleaned_data.get('email')

			email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )

			print("="*100)
			
			email.send()	

			print("="*100)

			return HttpResponse('Please confirm your email address to complete the registration')

	context = {
		"form":form,
	}

	return render(request,'signup.html',context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        print("ACTIBATE ",uid)

        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def test_view(request):

	return HttpResponse("Hello from django 2")

def greet_view(request):

	return HttpResponse("Employee greet")

def greet_view_with_param(request, name):

	context = {
		"name": name,
	}

	messages.success(request,"This is django success message")

	messages.error(request,"This is django error message")

	return render(request,"greet.html",context)

