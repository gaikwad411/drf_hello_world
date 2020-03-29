from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
