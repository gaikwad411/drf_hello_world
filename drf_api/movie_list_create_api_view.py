from rest_framework.generics import ListCreateAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

"""

curl -d "{\"title\": \"New Movie\", \"director\":\"New Director\"}" -H "Content-Type: application/json" -X POST http://localhost:8000/movie-list-create-api/

"""