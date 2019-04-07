from django.contrib import admin
from .models import Desktop, Laptop

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):

	list_display = ("name",'price','status','issue')
	
	list_filter = ('status','issue')


admin.site.register(Desktop,DeviceAdmin)

admin.site.register(Laptop,DeviceAdmin)
