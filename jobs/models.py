# jobs/models.py
import uuid
from django.db import models
from django.utils import timezone
from django.db.models import Q


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, db_index=True)
    grade = models.CharField(max_length=512,  db_index=True)
    code = models.JSONField(default=list, blank=True, db_index=True)
    group_type = models.CharField(max_length=255,  db_index=True)
    general_group = models.CharField(max_length=255,  db_index=True)
    job_location = models.CharField(max_length=512,  db_index=True)
    job_responsibilities = models.JSONField(
        default=list, blank=True, db_index=True)
    job_objectives = models.TextField(db_index=True)
    description = models.TextField(db_index=True)
    generated = models.TextField(db_index=True)
    objectives = models.TextField(db_index=True)
    skills = models.TextField(db_index=True)
    training = models.TextField(db_index=True)
    job_requirements = models.JSONField(
        default=list, blank=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        db_table = 'jobs'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['title']
        indexes = [
            models.Index(
                fields=[
                    'title', 'grade', 'group_type', 'general_group',
                    'job_location', 'job_responsibilities', 'job_objectives',
                    'description', 'generated', 'objectives', 'skills', 'training',
                ]
            ),
        ]

    @classmethod
    def full_text_search(cls, query: str):
        queryset = Q()
        for word in query.split():
            queryset |= Q(title__icontains=word)
            queryset |= Q(grade__icontains=word)
            queryset |= Q(group_type__icontains=word)
            queryset |= Q(general_group__icontains=word)
            queryset |= Q(job_location__icontains=word)
            queryset |= Q(job_responsibilities__icontains=word)
            queryset |= Q(job_objectives__icontains=word)
            queryset |= Q(description__icontains=word)
            queryset |= Q(generated__icontains=word)
            queryset |= Q(objectives__icontains=word)
            queryset |= Q(skills__icontains=word)
            queryset |= Q(training__icontains=word)
        return cls.objects.filter(queryset)

    def __str__(self):
        return self.title
