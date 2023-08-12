# views.py 
from django.shortcuts import render
from django.http import HttpResponse
from .models import JobDescription

# Placeholder view (Adjust based on what you want to display or actions you want to support)
def job_description_list(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not authorized to view this page.")
    
    descriptions = JobDescription.objects.all()
    
    return render(request, "job_description_list.html", {"descriptions": descriptions})
