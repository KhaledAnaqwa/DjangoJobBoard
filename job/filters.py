import django
import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    # salary = django_filters.NumberFilter(field_name='salary', lookup_expr='salary_gt')
    salary = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')


    class Meta:
        model = Job
        fields = '__all__'
        exclude =['image','id','slug','published_at','owner','vacances']