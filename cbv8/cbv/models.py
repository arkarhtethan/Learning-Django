from django.db import models

# Create your models here.

class ProductQuerySet(models.QuerySet):

	def drink(self):

		return self.filter(category="DRINK")

	def food(self):

		return self.filter(category='FOOD')

	def noodle(self):

		return self.filter(category="NOODLE")

class ProductManager(models.Manager):

	def get_queryset(self):

		return ProductQuerySet(self.model, using=self._db)

	def drink(self):

		return self.get_queryset().drink()

	def food(self):

		return self.get_queryset().food()

	def noodle(self):

		return self.get_queryset().noodle()

class Product(models.Model):

	choice = (

		("DRINK","Drink"),

		("NOODLE","Noodle"),

		("FOOD","Food"),

	)

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=1)

	category = models.CharField(max_length=120,choices=choice)

	categories = ProductManager()

	def __str__(self):

		return self.name
