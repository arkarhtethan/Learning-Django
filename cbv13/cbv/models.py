from django.db import models

# Create your models here.

class Product(models.Model):

	choice = (

		("DRINK","Drink"),
		("FOOD","Food"),
		("NOODLE","Noodle"),

	)

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=0)

	category = models.CharField(max_length=120,choices=choice)

	def __str__(self):

		return self.name

