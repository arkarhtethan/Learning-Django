from django.db import models

# Create your models here.

class Device(models.Model):

	choice = (

		("SOLD","Item sold out"),
		
		("RESTOCKING","Item will be restock in a few day"),
		
		("AVAILABLE","Item ready to be purchase"),

	)

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=0)

	status = models.CharField(max_length=120,choices=choice,default='AVAILABLE')

	class Meta:

		abstract = True


	def __str__(self):

		return self.name


class Desktop(Device):
	pass

class Laptop(Device):
	pass