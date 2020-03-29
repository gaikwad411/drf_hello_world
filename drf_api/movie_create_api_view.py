from rest_framework.generics import CreateAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieCreateAPIView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
