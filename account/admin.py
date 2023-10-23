from django.contrib import admin
from .models import Customer, Commment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'travel')
    list_display_links = list_display


@admin.register(Commment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'created_at')
    list_display_links = list_display
