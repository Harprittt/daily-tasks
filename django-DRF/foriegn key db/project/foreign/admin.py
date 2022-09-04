from django.contrib import admin
from . models import Post


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'page_title', 'page_cat', 'page_publish_date']
