import os
import random
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

def get_filename_ext(filename):

	return os.path.splitext(filename)

def image_upload_path(instance, filename):

	new_filename = random.randint(1,11111111111111111)

	_, ext = get_filename_ext(filename=filename)

	return 'product/{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)

class Product(models.Model):

	name = models.CharField(max_length=120)

	price = models.IntegerField(default=1)

	slug = models.SlugField(null=True, blank=True, unique=True)

	description = models.TextField(null=True, blank=True)

	image = models.ImageField(upload_to=image_upload_path,null=True, blank=True)

	active = models.BooleanField(default=True)

	featured = models.BooleanField(default=False)

	def __str__(self):

		return self.name


def product_pre_save(instance, sender, *args, **kwargs):

	if not instance.slug:

		instance.slug = unique_slug_generator(instance=instance)

pre_save.connect(product_pre_save, sender=Product)