from isort import api
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework import generics


@api_view(['GET'])
def JobListApi(request):
    all_data = Job.objects.all()
    data = JobSerializer(all_data,many=True).data

    return Response(data)