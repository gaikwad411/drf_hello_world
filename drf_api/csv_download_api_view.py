import os
import csv


from django.http import HttpResponse
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings


class CSVDownloadViewSet(APIView):

    def get(self, request, format=None):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="csv_data.csv"'
        writer = csv.DictWriter(response, fieldnames=['title', 'director'])
        writer.writeheader()
        writer.writerow({'title': 'Jumanji: The Next Level', 'director': 'Jake Kasdan'})
        return response


class FileDownloadAPIView(APIView):

    def get(self, request, format=None):
        file_location = os.path.join(settings.BASE_DIR, 'sample_files', 'movies.csv')

        try:
            with open(file_location, 'r') as f:
                file_data = f.read()

                # sending response
                response = HttpResponse(file_data, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="movies.csv"'

        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound('<h1>File not exist</h1>')

        return response
