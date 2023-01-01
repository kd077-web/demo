from django.contrib import admin
from practice.models import practiceadmin
class practices(admin.ModelAdmin):
    list_display=('title_icon','desc_icon')
admin.site.register(practiceadmin,practices)    

# Register your models here.
