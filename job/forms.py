from django import forms
from django.db.models import fields
from django.db.models.base import Model

from job.models import Apply,Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','website','cv','cover_latter']

class AddJobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields=['title','job_type','description','vacances','salary','image','category','experience']
