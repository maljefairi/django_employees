from .models import Job
from django import forms
from crispy_forms.helper import FormHelper

from .models import Job
from django import forms
from crispy_forms.helper import FormHelper


class JobForm(forms.ModelForm):
    code1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    code2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    code3 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    code4 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Job
        fields = [
            'title', 'grade', 'group_type', 'general_group',
            'job_location', 'job_responsibilities', 'job_objectives',
            'job_requirements', 'description', 'generated', 'objectives', 'skills', 'training',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        # add form-control class to all input fields
        codes = self.instance.code if self.instance and self.instance.code else [
            None, None, None, None]

        # Populate the form fields with the values from the 'code' JSON field
        self.fields['code1'].initial = codes[0] if len(codes) > 0 else ''
        self.fields['code2'].initial = codes[1] if len(codes) > 1 else ''
        self.fields['code3'].initial = codes[2] if len(codes) > 2 else ''
        self.fields['code4'].initial = codes[3] if len(codes) > 3 else ''
        # add form-control class to all input fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.code = [
            self.cleaned_data['code1'],
            self.cleaned_data['code2'],
            self.cleaned_data['code3'],
            self.cleaned_data['code4']
        ]
        if commit:
            instance.save()
        return instance


class JobFilterForm(forms.Form):
    title = forms.CharField(required=False)
    grade = forms.CharField(required=False)
    group_type = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
