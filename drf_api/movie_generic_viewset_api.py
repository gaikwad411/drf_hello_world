from rest_framework.viewsets import GenericViewSet
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, \
    RetrieveModelMixin, DestroyModelMixin


class MovieGenericViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin,
                          RetrieveModelMixin, DestroyModelMixin,
                          GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
