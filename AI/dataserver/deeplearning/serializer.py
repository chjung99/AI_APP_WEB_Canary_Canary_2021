from rest_framework import serializers

from .models import File, TrainedModel

class FileSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)
    
    def create(self, validated_data):
        file = File.objects.create(
            file=validated_data['file']
        )
        
        file.save()
        return file
        

class TrainModelSerializer(serializers.Serializer):
    file = serializers.FileField(required=True)
    result = serializers.FileField(required=True)
    version = serializers.IntegerField(required=True)
