from rest_framework.generics import ListAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
