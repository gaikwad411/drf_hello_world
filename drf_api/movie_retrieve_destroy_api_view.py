from rest_framework.generics import RetrieveDestroyAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
