# api/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, Sprint, Task, Incident, Comment

class CustomUserAdmin(UserAdmin):
    # Agrega tus campos personalizados a la vista de lista
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')
    
    # Agrega los campos al formulario de edición del usuario
    # Se basa en los fieldsets de UserAdmin y añade el tuyo
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'avatar')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role', 'avatar')}),
    )

# Registra tu modelo User con la clase admin personalizada
admin.site.register(User, CustomUserAdmin)
admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(Incident)
admin.site.register(Comment)
