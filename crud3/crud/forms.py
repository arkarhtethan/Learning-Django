
from django import forms
from .models import Laptop,Desktop

class LaptopForm(forms.ModelForm):

	class Meta:

		model = Laptop

		fields = "__all__"

		widgets = {

		"name" : forms.TextInput(

			attrs={

				"class":"form-control mb-4",

				"placeholder":"Enter Laptop Name"

			}

		),

		"price" : forms.NumberInput(

			attrs={

				"class":"form-control mb-4",

				"placeholder":"Enter Laptop Price"

			}

		),

		"issue" : forms.TextInput(

			attrs={

				"class":"form-control mb-4",

				"placeholder":"Enter Laptop issue"

			}

		),


	}



class DesktopForm(forms.ModelForm):

	class Meta:

		model = Desktop

		fields = "__all__"

		widgets = {

				"name" : forms.TextInput(

					attrs={

						"class":"form-control mb-4",

						"placeholder":"Enter Desktop Name"

					}

				),

				"price" : forms.NumberInput(

					attrs={

						"class":"form-control mb-4",

						"placeholder":"Enter Desktop Price"

					}

				),

				"issue" : forms.TextInput(

					attrs={

						"class":"form-control mb-4",

						"placeholder":"Enter Desktop issue"

					}

				),


			}

