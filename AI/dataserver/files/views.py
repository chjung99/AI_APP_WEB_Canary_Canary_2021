from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializer import FilesSerializer
from .models import Files

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
    
