from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as drf_filters
from jobs.models import Job


class JobFilter(drf_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'title': ['icontains'],
            'grade': ['exact'],
            'group_type': ['exact'],
            'general_group': ['exact'],
            'job_location': ['exact'],
            'job_responsibilities': ['icontains'],
            'job_objectives': ['icontains'],
            'job_requirements': ['icontains'],
            'description': ['icontains'],
            'generated': ['exact'],
            'objectives': ['icontains'],
            'skills': ['icontains'],
            'training': ['icontains'],
            'created_at': ['exact', 'gte', 'lte'],
        }


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id',
                  'title', 'grade', 'group_type', 'general_group', 'code',
                  'job_location', 'job_responsibilities', 'job_objectives',
                  'job_requirements', 'description', 'generated', 'objectives', 'skills', 'training', 'created_at')
        read_only_fields = ('id', 'created_at',)


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filterset_class = JobFilter

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
