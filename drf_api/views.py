from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view()
def hello_world_api(request):
    return Response({"message": "Hello, world!"})


class HelloWorldAPIView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})
