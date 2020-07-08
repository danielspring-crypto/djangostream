from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.site_header = 'Django Stream Admin Panel'
admin.site.site_title = 'Django Stream'
admin.site.index_title = 'Django Admin'

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'text', 'image', 'date']
	list_filter = ['date']
	search_fields = ['title',]

admin.site.register(Post, PostAdmin)