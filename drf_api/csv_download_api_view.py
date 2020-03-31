import csv
from django.http import HttpResponse
from rest_framework.views import APIView


class CSVDownloadViewSet(APIView):

    def get(self, request, format=None):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="csv_data.csv"'
        writer = csv.DictWriter(response, fieldnames=['title', 'director'])
        writer.writeheader()
        writer.writerow({'title': 'Jumanji: The Next Level', 'director': 'Jake Kasdan'})
        return response
