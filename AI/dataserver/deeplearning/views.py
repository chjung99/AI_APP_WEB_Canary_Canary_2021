from multiprocessing import Process

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializer import FileSerializer, TrainModelSerializer
from .models import File, TrainedModel
from .train_with_azure import train

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    
class TrainModelViewSet(viewsets.ModelViewSet):
    dataset_file = File.objects.all()
    dataset_serializer_class = FileSerializer
    
    queryset = TrainedModel.objects.all()
    serializer_class = TrainModelSerializer
    
    def create(self, request, *args, **kwargs):
        file = self.dataset_file.latest('upload_at')
        serializer = self.dataset_serializer_class(file)
        
        p = Process(target=train, args=(serializer.data['file'], 1, ))
        p.start()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().latest('version')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        