from django.contrib import admin

# Register your models here.

from . models import contact

class contactAdmin(admin.ModelAdmin):
    list_display=('name', 'mail', 'number', 'sms')
admin.site.register(contact, contactAdmin)

