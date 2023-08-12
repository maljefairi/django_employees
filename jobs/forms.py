# jobs/forms.py 
from .models import JobDescription
from django import forms

class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = '__all__'


class JobDescriptionFilterForm(forms.Form):
    title = forms.CharField(required=False)
    grade = forms.CharField(required=False)
    group_type = forms.CharField(required=False)

