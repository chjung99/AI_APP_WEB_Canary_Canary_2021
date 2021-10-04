from rest_framework import serializers

from .models import Files

class FilesSerializer(serializers.Serializer):
    files = serializers.FileField(required=True)

    def create(self, validated_data):
        user = Files.objects.create(
            files=validated_data['files'],
        )

        user.save()
        return user  