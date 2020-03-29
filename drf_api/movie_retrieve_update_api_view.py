from rest_framework.generics import RetrieveUpdateAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
