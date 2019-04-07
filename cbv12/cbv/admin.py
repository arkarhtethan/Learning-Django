from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(ImportExportModelAdmin):

	list_display = ("name","price",'category')

	list_editable = ("price",'category')

	list_filter = ("category",)


admin.site.register(Product, ProductAdmin)
