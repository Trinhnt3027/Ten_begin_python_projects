from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')

# Register your models here.
admin.site.register(Post, PostAdmin)
