from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site

from .forms import SignUpForm
from django.contrib.auth.models import User
# email 
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text



# Create your views here.
def register_view(request):

	form = SignUpForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():

			user = form.save(commit=False)

			user.is_active = False

			user.save()

			# send email

			current_site = get_current_site(request)

			email_subject = "ACTIVATE YOUR BLOG ACCOUNT"

			message = render_to_string('activate_email.html',{
				"user":user,
				"domain":current_site.domain,
				"uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				"token": account_activation_token.make_token(user),
				})

			to_email = form.cleaned_data['email']

			email = EmailMessage(
					email_subject,
					message,
					to=[to_email]
				)

			email.send()

			return HttpResponse("Activation Link is sent to your email account.")

	context = {
		"form":form,
	}

	return render(request,'signup.html',context)

def activate_view(request, uidb64, token):

	try:

		uuid = force_text(urlsafe_base64_decode(uidb64))

		user = User.objects.get(pk=uuid)

	except(User.DoesNotExist, ValueError, TypeError, OverflowError):

		user = None

	if user is not None and account_activation_token.check_token(user, token):

		user.is_active = True

		user.save()

		login(request, user)

		return HttpResponse("Successfully activate your account ")

	else:

		return HttpResponse("Verification link invalid")
