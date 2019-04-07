from django.db import models

# Create your models here.

PRODUCT_TYPE = (
	("drink","Drink"),
	("noodle","Noodle"),
	("snack","Snack"),
)

class Product(models.Model):

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=10)

	type_of_product = models.CharField(max_length=120,choices=PRODUCT_TYPE)

	def __str__(self):

		return self.name