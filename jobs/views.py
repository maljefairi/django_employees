from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.db.models import Q
from .utils import search_with_aprox


def employee_list(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not authorized to view this page.")

    search_name = request.POST.get("name", "")
    search_nationality = request.POST.get("nationality", "")
    search_job_title = request.POST.get("job_title", "")
    search_job_number = request.POST.get("job_number", "")

    search_keyword = request.POST.get("keyword", "")

    employees = Employee.objects.all()

    if search_keyword:
        employees = search_with_aprox(search_keyword, employees)
    else:
        if search_name:
            employees = employees.filter(name__icontains=search_name)
        if search_nationality:
            employees = employees.filter(nationality__icontains=search_nationality)
        if search_job_title:
            employees = employees.filter(job_title__icontains=search_job_title)
        if search_job_number:
            employees = employees.filter(job_number=search_job_number)

    return render(request, "employee_list.html", {"employees": employees})
