from django.contrib import admin
from .models import Desktop,Laptop

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):

	list_display = ("name","price","issue","status")

	list_editable = ("price","issue","status")

	list_filter = ("issue","status")

admin.site.register(Desktop, DeviceAdmin)
admin.site.register(Laptop, DeviceAdmin)
