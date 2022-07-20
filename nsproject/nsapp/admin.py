from django.contrib import admin
from .models import User, Project, Client
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'user']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'project']
