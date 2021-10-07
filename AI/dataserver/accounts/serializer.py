from rest_framework import serializers

from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User, update_last_login
from django.contrib.auth import authenticate

JWT_PLAYLOAD_HANDLER = api_settings.JWT_PLAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)
    tocken = serializers.CharField(max_length=255, read_only=True)
    
    
    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)
        
        if user is None:
            return { 'username': None }
        try:
            playload = JWT_PLAYLOAD_HANDLER(user)
            jwt_tocken = JWT_ENCODE_HANDLER(playload)
            update_last_login(None, user)
        
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does net exists.'
            )
        return {
            'username': user.username,
            'tocken': jwt_tocken,
        }