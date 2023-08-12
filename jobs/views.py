from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)
from django.views.generic.detail import DetailView
from django.urls import reverse


from .models import Job
from .forms import JobForm, JobFilterForm


class JobDescriptionDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_description_detail.html'
    context_object_name = 'job_description'
    form_class = JobForm

    def get_object(self):
        return get_object_or_404(Job, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.get_object())
        return context


def job_description_list(request: HttpRequest):
    queryset = Job.objects.all()

    form = JobFilterForm(request.GET or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        grade = form.cleaned_data.get('grade')
        group_type = form.cleaned_data.get('group_type')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if grade:
            queryset = queryset.filter(grade__icontains=grade)
        if group_type:
            queryset = queryset.filter(group_type__icontains=group_type)

    paginator = Paginator(queryset, 100)
    page = request.GET.get('page')
    try:
        job_descriptions = paginator.page(page)
    except PageNotAnInteger:
        job_descriptions = paginator.page(1)
    except EmptyPage:
        job_descriptions = paginator.page(paginator.num_pages)

    context = {
        'queryset': job_descriptions,
        'form': form
    }

    return render(request, 'jobs/job_description_list.html', context)


def job_description_detail(request: HttpRequest, pk):
    job_description = get_object_or_404(Job, pk=pk)
    context = {'form': job_description}
    return render(request, 'jobs/job_description_detail.html', context)


def job_description_create(request: HttpRequest):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('job_description_list')
    context = {'form': form}
    return render(request, 'jobs/job_description_form.html', context)


def job_description_edit(request: HttpRequest, pk):
    job_description = get_object_or_404(Job, pk=pk)
    form = JobForm(request.POST or None, instance=job_description)
    if form.is_valid():
        form.save()
        return redirect('job_description_list')
    context = {'form': form}
    return render(request, 'jobs/job_description_form.html', context)


def job_description_delete(request: HttpRequest, pk):
    queryset: Job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('job_description_list')
    context = {'form': queryset}
    return render(request, 'jobs/job_description_confirm_delete.html', context)


def home(request):
    return render(request, 'jobs/home.html')
