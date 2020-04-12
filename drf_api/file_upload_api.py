"""

1. File upload using db model
2. File upload without db model
3. Multiple file uploads


"""
from rest_framework.views import APIView
from .serializers import MovieSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from django.core.files import File
from django.core.files.storage import default_storage


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
    """

    curl -X POST -H "Content-Type: multipart/form-data"
    -F "file=@poster.png"
    http://localhost:8000/file-upload-without-db-model-api/

    """
    parser_class = (FileUploadParser, )

    def post(self, request):
        if 'file' not in request.data:
            raise ParseError("Empty content")

        f = request.data['file']

        try:
            myfile = File(f)
            default_storage.save(myfile.name, myfile)
        except Exception as e:
            print(e)
            raise ParseError("Could not process file")

        return Response({"status": "success"}, status=status.HTTP_200_OK)


class MultipleFilesUpload(APIView):
    """
    curl -X POST -H "Content-Type: multipart/form-data" -F "files=@poster.png" -F "files=@poster.png"
    http://localhost:8000/multiple-file-uploads-api/

    """

    def post(self, request):
        files = dict(request.data.lists())['files']

        try:
            for file in files:
                myfile = File(file)
                default_storage.save(myfile.name, myfile)
        except Exception as e:
            print(e)
            raise ParseError("Could not process file")

        return Response({"status": "success"}, status=status.HTTP_200_OK)
