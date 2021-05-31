from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test APIView"""


    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django view'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})