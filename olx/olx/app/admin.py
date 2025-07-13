from django.contrib import admin
from .models import Category, Ad

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'author', 'category', 'created_at')
    list_filter = ('category', 'location', 'created_at')
    search_fields = ('title', 'description', 'location')
