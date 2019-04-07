from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):

	list_display = ("name","price","type_of_product")

	list_filter = ("type_of_product",)

	list_editable = ("price","type_of_product")



admin.site.register(Product,ProductAdmin)
