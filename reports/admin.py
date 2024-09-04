from django.contrib import admin
from .models import Task, Project

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'status', 'due_date', 'description')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('due_date',)




class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('department', 'created_at')

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)