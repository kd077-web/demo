from django.contrib import admin
from service.models import services
class serviceadmin(admin.ModelAdmin):
    list_display=('title','desc')
admin.site.register(services,serviceadmin)    

# Register your models here.
