from django.contrib import admin

from . models import donarList

class dlistAdmin(admin.ModelAdmin):
    list_display=('name', 'mail', 'number')
admin.site.register(donarList, dlistAdmin)

