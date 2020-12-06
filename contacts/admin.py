from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing',
                    'email', 'contact_date',)
    list_display_link = ('id', 'name',)
    list_filter = ('name', )
    list_editable = ('name', )
    search_fields = ['id', 'name', 'listing',
                     'email', 'contact_date']
    list_per_page = 25


# Register your models here.
admin.site.register(Contact, ContactAdmin)
