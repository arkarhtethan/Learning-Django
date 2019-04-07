from django.contrib import admin
from .models import Desktop,Laptop
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):

	list_display = ('name','price','status')

	list_filter = ("status",)

	list_editable = ('price','status',)

admin.site.register(Desktop,DeviceAdmin)
admin.site.register(Laptop,DeviceAdmin)
