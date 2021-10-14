from django.db import reset_queries
from django.db.models import Count
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response 
from rest_framework import serializers, status
from .models import Job, Skill
from .serializers import SkillSerializer, SkillReadSerializer, JobSerializer, JobOnlyReadSerializer
from rest_framework.viewsets import ModelViewSet

class CreateSkill(CreateAPIView):
    """ Handle the skills creation """
    serializer_class = SkillSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'skill': serializer.data}, 
                            status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
class CreateJob(CreateAPIView):
    """ Handle the jobs creation"""
    serializer_class = JobSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'job': serializer.data}, 
                            status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ListJob(ListAPIView):
    """ Handle the jobs list """
    serializer_class = JobOnlyReadSerializer
    
    def get_queryset(self):
        return Job.objects.all()
    
class RetrieveJob(RetrieveAPIView):
    """ Retrieve a job"""
    serializer_class = JobOnlyReadSerializer
    
    def get_queryset(self, pk=None):
        if pk:
            return Job.objects.get(id = pk)

class Skills(ListAPIView): 
    """Shows how many jobs each skill appears in"""
    serializer_class = SkillReadSerializer
    
    def get_queryset(self):
        return Skill.objects.all().annotate(num_job=Count('job'))
    