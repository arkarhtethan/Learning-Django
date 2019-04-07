from django.db import models

# Create your models here.

class Device(models.Model):

	choice = (

		('AVAILABLE',"Item ready to purchased"),
		
		('SOLD',"Item sold out"),

		('RESTOCKING',"Item will be stock in a few day"),

	)

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=0)

	issue = models.CharField(max_length=120,default='No issue')

	status = models.CharField(max_length=120,default='AVAILABLE',choices=choice)

	def __str__(self):

		return self.name

	class Meta:

		abstract = True

class Desktop(Device):
	pass

class Laptop(Device):
	pass