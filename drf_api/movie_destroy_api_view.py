from rest_framework.generics import DestroyAPIView
from .models import Movie
from .serializers import MovieSerializer


class MovieDestroyAPIView(DestroyAPIView):
    queryset = Movie.objects.all()
