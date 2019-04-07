from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Product(models.Model):

	choices = (

		("SNACK","Snack"),

		("DRINK","Drink"),

		("FOOD","Food"),

	)

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=1)

	category = models.CharField(max_length=120,choices=choices,blank=True)

	class Meta:

		ordering = ("id",)

	def get_absolute_url(self):

		return reverse(
			'product-detail',
			kwargs={"pk":self.pk}
			)

	def __str__(self):

		return self.name



