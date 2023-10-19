from django.contrib import admin
from .models import Travel, Post

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'active', 'departure')
    list_display_links = list_display

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = list_display

