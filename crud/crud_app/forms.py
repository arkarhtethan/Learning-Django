from django import forms
from .models import Desktop,Laptop

class LaptopForm(forms.ModelForm):

	class Meta:

		model = Laptop

		fields = "__all__"


class DesktopForm(forms.ModelForm):

	class Meta:

		model = Desktop

		fields = "__all__"

		widgets = {

			"name":forms.TextInput(

				attrs={

					"class":"form-control mb-4",

					"placeholder":"Enter Desktop Name"

				}
			),

			"price":forms.NumberInput(

				attrs={

					"class":"form-control mb-4",
					
					"placeholder":"Enter Desktop Price"

				}
			),


		}

class LaptopForm(forms.ModelForm):

	class Meta:

		model = Laptop

		fields = "__all__"

		widgets = {

			"name":forms.TextInput(

				attrs={

					"class":"form-control mb-4",

					"placeholder":"Enter Laptop Name"

				}
			),

			"price":forms.NumberInput(

				attrs={

					"class":"form-control mb-4",
					
					"placeholder":"Enter Laptop Price"

				}
			),


		}

