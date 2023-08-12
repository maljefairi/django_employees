# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.job_description_list,  name='job_description_list'),
    path('job/<uuid:pk>/', views.JobDescriptionDetailView.as_view(),
         name='job_description_detail'),
    path('job/new/', views.job_description_create,
         name='job_description_create'),
    path('job/<uuid:pk>/edit/',  views.job_description_edit,
         name='job_description_edit'),
    path('', views.home, name='index'),
    path('job/<uuid:pk>/delete/',
         views.job_description_delete, name='job_description_delete'),
]
