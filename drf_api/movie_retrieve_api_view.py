from rest_framework.generics import RetrieveAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieRetrieveAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
