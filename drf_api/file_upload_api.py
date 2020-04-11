"""

1. File upload using db model
2. File upload without db model
3. Multiple file uploads
4. File upload along with data

"""
from rest_framework.views import APIView
from .serializers import MovieSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status


class FileUploadUsingDBModel(APIView):
    """

    curl -X POST -H "Content-Type: multipart/form-data"
    -F "title=movie1" -F "director=director1" -F "poster=@poster.png"
    http://localhost:8000/file-upload-using-db-model-api/

    """
    parser_class = (FileUploadParser, )

    def post(self, request):
        file_serializer = MovieSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadWithoutDBModel(APIView):
    pass


class MultipleFileUploads(APIView):
    pass


class FileUploadAlongWithData(APIView):
    pass
