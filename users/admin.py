from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Custom Fields', {'fields': ('lavozimi',)}),
    )
    list_display = ('username','password', 'lavozimi', 'is_staff', 'is_superuser')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser', 'lavozimi'),
        }),
    )
    search_fields = ('username', 'lavozimi')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
