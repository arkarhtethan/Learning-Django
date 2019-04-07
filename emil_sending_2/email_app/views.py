from .forms import SignUpForm
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Create your views here.
def register_view(request):

	form  = SignUpForm(request.POST or None)

	if request.method == "POST":

		if form.is_valid():

			user = form.save(commit=False)

			user.is_active = False

			user.save()

			current_site = get_current_site(request)

			subject = "Activate your account."

			message = render_to_string(
	
					'email_template.html', {

						"user":user,

						"domain":current_site.domain,

						"uidb64":urlsafe_base64_encode(force_bytes(user.pk)).decode(),

						"token":account_activation_token.make_token(user),

					}
				)

			to_email = form.cleaned_data['email']

			email = EmailMessage(subject,message,to=[to_email])

			email.send()

			# send email

			return HttpResponse("Activation link sent to your email account")

	context = {

		"form": form,

	}

	return render(request,"signup.html",context)

def activate_account_view(request, uidb64, token):

	try:

		uid = force_text(urlsafe_base64_decode(uidb64))

		user = User.objects.get(pk=uid)

	except (User.DoesNotExist, ValueError, OverflowError, TypeError):

		user = None

	if user is not None and account_activation_token.check_token(user, token):

		user.is_active = True

		user.save()

		login(request, user)

		return HttpResponse("Successfully activate your account.")

	else:

		return HttpResponse("Activation Link invalid")		

