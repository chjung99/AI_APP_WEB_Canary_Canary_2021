from rest_framework import serializers

from .models import File, TrainedModel, Log

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
    matrix = serializers.FloatField(required=True)


class LogModelSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    log = serializers.CharField(required=True)
    create_at = serializers.DateField(required=True)
    
    def create(self, validated_data):
        log = Log.objects.create(
            username=validated_data['username'],
            log=validated_data['log']
        )
        
        log.save()
        return log