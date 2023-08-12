# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_description_list, name="job_description_list"),
]
