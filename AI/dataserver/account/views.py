from rest_framework import viewsets, status
from rest_framework.response import Response

# from rest_framework_jwt.authentication import 

from .serializer import UserLoginSerializer

class Login(viewsets.ViewSet):
    def create(self, request, id=None):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
            
        if serializer.validated_data['username'] == None:
            return Response({'message': 'fail', 'token':'None'}, status=status.HTTP_200_OK)

        response = {
            'success': 'True',
            'token': serializer.data['token'],
        }
        return Response(response, status=status.HTTP_200_OK)