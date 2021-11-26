from django import forms
from django.db.models import fields
from django.db.models.base import Model

from job.models import Apply


class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','website','cv','cover_latter']