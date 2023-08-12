# admin.py 
from django.contrib import admin
from .models import JobTitle, JobDescription

admin.site.register(JobTitle)
admin.site.register(JobDescription)
