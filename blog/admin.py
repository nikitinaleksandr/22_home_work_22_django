from django.contrib import admin
from .models import Blog  # или Post, как называется ваша модель

@admin.register(Blog)  # если модель называется Blog
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'create_at', 'description', 'views_count')
