from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Request

class RequestAdmin(admin.ModelAdmin):
    search_fields = ('vehicle_name','customer')
    list_per_page = 10

admin.site.register(Request, RequestAdmin)