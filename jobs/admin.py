# admin.py
from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'grade', 'group_type',
                    'general_group', 'job_location', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'grade', 'group_type', 'general_group', 'job_location', 'job_responsibilities',
                     'job_objectives', 'job_requirements', 'description', 'generated', 'objectives', 'skills', 'training', 'created_at')
    readonly_fields = ('created_at',)
