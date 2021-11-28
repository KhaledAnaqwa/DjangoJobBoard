from isort import api
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


@api_view(['GET'])
def JobListApi(request):
    all_data = Job.objects.all()
    data = JobSerializer(all_data,many=True).data

    return Response(data)

@api_view(['GET'])
def JobDetailApi(request,id):
    all_data = Job.objects.get(id__exact=id)
    data = JobSerializer(all_data).data

    return Response(data)


class JobListApiV2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field='id'



class JobViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving jobs.
    """
    def list(self, request):
        queryset = Job.objects.all()
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Job.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
    

    
