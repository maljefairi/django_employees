# models.py
from django.db import models

class JobTitle(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class JobDescription(models.Model):
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    grade = models.CharField(max_length=100)
    code = models.TextField()  # Consider serialization techniques if storing lists
    group_type = models.CharField(max_length=100)
    general_group = models.CharField(max_length=100)
    job_location = models.TextField()
    job_responsibilities = models.TextField()
    job_objectives = models.TextField()  # Consider serialization techniques if storing lists
    job_requirements = models.TextField()  # Consider serialization techniques if storing lists
    description = models.TextField()
    generated = models.TextField()
    objectives = models.TextField()
    skills = models.TextField()
    training = models.TextField()

    def __str__(self):
        return self.job_title.title
