#-*- coding: utf-8 -*-
from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'first_name', 'last_name')
    search_fields = ['username', 'first_name', 'last_name']
    fieldsets = [
        ('Personal Information', {'fields': ['username', 'first_name', 'last_name', 'email', 'is_active',
         'is_superuser', 'is_staff', 'date_joined']}),
        ('Groups and Users', {'fields': ['groups', 'user_permissions']}),
    ]

admin.site.register(User, UserAdmin)
