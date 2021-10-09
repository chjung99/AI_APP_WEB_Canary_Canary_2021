from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import UserLoginSerializer

class Login(viewsets.ViewSet):
    def create(self, request, id=None):
        serializer = UserLoginSerializer(data=request.data)
        
        if not serializer.is_valid(raise_exception=True):
            return Response({'message': 'Request Body Error.'}, status=409)
        
        if serializer.validated_data['username'] == None:
            return Response({'message': 'fail'}, status=200)
            
        response = {
            'success': True,
            'tocken': serializer.data['token'],
        }
        
        return Response(response, status=200)