from django.db import models

# Create your models here.

class ProductQuerySet(models.query.QuerySet):

	def drink(self):

		return self.filter(category="DRINK")

	def food(self):

		return self.filter(category="FOOD")

	def snack(self):

		return self.filter(category="SNACK")

	def noodle(self):

		return self.filter(category="NOODLE")

class ProductManager(models.Manager):

	def get_queryset(self):

		return ProductQuerySet(self.model,using=self._db)

	def drink(self):

		return self.get_queryset().drink()

	def food(self):

		return self.get_queryset().food()

	def snack(self):

		return self.get_queryset().snack()

	def noodle(self):

		return self.get_queryset().noodle()

	def get_by_category(self,category):

		category = category.upper()

		return self.get_queryset().filter(category=category)

class Product(models.Model):

	CHOICE = (

		("FOOD",'Food'),
		("DRINK",'Drink'),
		("SNACK",'Snack'),
		("NOODLE",'Noodle'),
	)

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=1)

	category = models.CharField(max_length=120,choices=CHOICE,default='FOOD')

	objects = ProductManager()

	def __str__(self):

		return self.name

