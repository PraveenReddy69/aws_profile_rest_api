from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnPersmission
from rest_framework import filters

class HelloAPIview(APIView):
    """docstring for HelloAPIview."""
    serializer_class=serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of API Features"""

        an_apiview=[
        'Praveen Reddy',
        'Hutchie',
        'Kothi',
        'Kukka',
        ]

        return Response({'Message':'Hello','api_view':an_apiview})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """Updating the data"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Partially Updating the data"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Deleting the object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message."""
        ...

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnPersmission,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


