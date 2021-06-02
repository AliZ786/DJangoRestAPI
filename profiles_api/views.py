from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, models
from rest_framework import viewsets

class HelloAPIView(APIView):
    """Test APIView"""

    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django view'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk= None):
        """Handles updating an object"""
        return Response({'method': 'PUT'})         


    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'method': 'PATCH'})         

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [

            'Uses actions (list, create, retrieve, update, partIal_update)',
            'Automatically maps to URLs'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request ):
        """Creates a new message"""
        serializer = self.serializer_class(data=request.data)    

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"

            return Response({'message': message})

        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    


    def retreive(self, request, pk = None):
        """Handle getting an object by it's ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk = None):
        """Handles updating the object"""
        return Response({'http_method': 'PUT'})    

    def partial_update(self, request, pk = None):
        """Handles updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk = None):
        """Handles removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
