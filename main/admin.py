from django.contrib import admin
from .models import Blog, Tag

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'image', 'description', 'date', 'user']
	list_editable = ['title', 'description', 'date', 'user']
	ordering = ['-id']
	list_per_page = 4
	search_fields = ['name']

admin.site.register(Blog)
admin.site.register(Tag)