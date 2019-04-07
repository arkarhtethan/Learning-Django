from django.db import models

# Create your models here.

class Device(models.Model):

	choice = (
		("AVAIABLE",'Item can be purchase'),
		
		("RESTOCKING",'Item will be restock in a few day'),

		("SOLD",'Item Sold out'),
	)

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=0)

	status = models.CharField(max_length=120,choices=choice)

	issue = models.CharField(max_length=120,default="No issue")

	def __str__(self):

		return self.name

	class Meta:

		abstract = True

class Desktop(Device):
	pass

class Laptop(Device):
	pass
