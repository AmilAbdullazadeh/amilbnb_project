from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor',)
    list_display_link = ('id', 'title',)
    list_filter = ('realtor', )
    list_editable = ('is_published', )
    search_fields = ['title', 'description',
                     'price', 'list_date', 'city', 'state', 'zipcode']
    list_per_page = 25


# Register your models here.
admin.site.register(Listing, ListingAdmin)
