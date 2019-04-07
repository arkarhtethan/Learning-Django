from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):

	list_display = ("name",'price','category')

	list_editable = ("price",'category')

	list_filter = ("category",)

	search_fields = ("name",'price','category')


admin.site.register(Product, ProductAdmin)

