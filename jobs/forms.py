from .models import Job
from django import forms
from crispy_forms.helper import FormHelper


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            'title', 'grade', 'code', 'group_type', 'general_group',
            'job_location', 'job_responsibilities', 'job_objectives',
            'description', 'generated', 'objectives', 'skills', 'training',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False


class JobFilterForm(forms.Form):
    title = forms.CharField(required=False)
    grade = forms.CharField(required=False)
    group_type = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
