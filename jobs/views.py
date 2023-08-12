from django.shortcuts import render, redirect, get_object_or_404
from .models import JobDescription
from .forms import JobDescriptionForm, JobDescriptionFilterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def job_description_list(request):
    job_descriptions = JobDescription.objects.all()

    form = JobDescriptionFilterForm(request.GET or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        grade = form.cleaned_data.get('grade')
        group_type = form.cleaned_data.get('group_type')

        if title:
            job_descriptions = job_descriptions.filter(job_title__title__icontains=title)
        if grade:
            job_descriptions = job_descriptions.filter(grade__icontains=grade)
        if group_type:
            job_descriptions = job_descriptions.filter(group_type__icontains=group_type)

    paginator = Paginator(job_descriptions, 100)  # Show 100 items per page
    page = request.GET.get('page')
    try:
        job_descriptions = paginator.page(page)
    except PageNotAnInteger:
        job_descriptions = paginator.page(1)
    except EmptyPage:
        job_descriptions = paginator.page(paginator.num_pages)

    context = {
        'job_descriptions': job_descriptions,
        'form': form
    }

    return render(request, 'jobs/job_description_list.html', context)

def job_description_detail(request, pk):
    job_description = get_object_or_404(JobDescription, pk=pk)
    context = {
        'job_description': job_description
    }
    return render(request, 'jobs/job_description_detail.html', context)

def job_description_create(request):
    form = JobDescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('job_description_list')
    context = {
        'form': form
    }
    return render(request, 'jobs/job_description_form.html', context)

def job_description_edit(request, pk):
    job_description = get_object_or_404(JobDescription, pk=pk)
    form = JobDescriptionForm(request.POST or None, instance=job_description)
    if form.is_valid():
        form.save()
        return redirect('job_description_list')
    context = {
        'form': form
    }
    return render(request, 'jobs/job_description_form.html', context)

def job_description_delete(request, pk):
    job_description = get_object_or_404(JobDescription, pk=pk)
    if request.method == "POST":
        job_description.delete()
        return redirect('job_description_list')
    context = {
        'job_description': job_description
    }
    return render(request, 'jobs/job_description_confirm_delete.html', context)

def home(request):
    return render(request, 'jobs/home.html')
