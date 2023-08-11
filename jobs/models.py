from django.db import models


class Employee(models.Model):
    job_number = models.IntegerField()
    name = models.CharField(max_length=500, null=True, blank=True)
    personal_number = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=500, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    administration = models.CharField(max_length=200, null=True, blank=True)
    qualification = models.CharField(max_length=150, null=True, blank=True)
    major = models.CharField(max_length=150, null=True, blank=True)
    degree = models.CharField(max_length=100, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    job_duties = models.TextField(null=True, blank=True)
    job_objectives = models.TextField(null=True, blank=True)
    suggested_training = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
