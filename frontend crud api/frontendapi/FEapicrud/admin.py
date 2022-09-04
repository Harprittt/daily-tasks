from django.contrib import admin
from .models import Novel

# Register your models here.


@admin.register(Novel)

class NovelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'description','publisher']