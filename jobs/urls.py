# jobs/urls.py
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('job_descriptions/', views.job_description_list, name='job_description_list'),
    path('job_descriptions/<int:pk>/', views.job_description_detail, name='job_description_detail'),
    path('job_descriptions/new/', views.job_description_create, name='job_description_create'),
    path('job_descriptions/<int:pk>/edit/', views.job_description_edit, name='job_description_edit'),
    path('', views.home, name='index'),
    path('job_descriptions/<int:pk>/delete/', views.job_description_delete, name='job_description_delete'),

]
