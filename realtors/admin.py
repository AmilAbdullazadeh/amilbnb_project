from django.contrib import admin

# Register your models here.
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date', )
    list_display_link = ('id', 'name',)
    search_fields = ['name']
    list_per_page = 25


# Register your models here.
admin.site.register(Realtor, RealtorAdmin)
