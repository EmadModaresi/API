from django.contrib import admin
from API.models import Book


class AdminMode(admin.ModelAdmin):
    list_display = ['author' , 'store_name' , 'fav' , 'create_at']
    search_fields = ['author' , 'store_name']

admin.site.register(Book ,AdminMode)
