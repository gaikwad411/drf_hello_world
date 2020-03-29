from rest_framework.generics import UpdateAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieUpdateAPIView(UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
