from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

	def clean(self):

		data = self.cleaned_data

		password = data['password']

		password2 = data['password2']

		username = data['username']

		qs = User.objects.filter(username=username)

		if qs.exists():
			
			raise forms.ValidationError("Username already exists")


		if password != password2:

			raise forms.ValidationError("You need to enter the same password")



		return data
