from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Movie
from .serializers import MovieSerializer


class MovieReadOnlyModelViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
