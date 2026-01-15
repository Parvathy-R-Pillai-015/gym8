from django.contrib import admin
from .models import UserLogin

# Register your models here.

@admin.register(UserLogin)
class UserLoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'emailid', 'role', 'is_active', 'created_at')
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('name', 'emailid')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('User Information', {
            'fields': ('name', 'emailid', 'password', 'role')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
