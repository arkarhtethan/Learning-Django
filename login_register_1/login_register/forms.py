from django import forms

class LoginForm(forms.Form):

	username = forms.CharField(max_length=120)
	
	password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):

	username = forms.CharField(max_length=120)
	
	email = forms.EmailField()
	
	password1 = forms.CharField(widget=forms.PasswordInput, label="Passowrd")
	
	password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Passowrd")