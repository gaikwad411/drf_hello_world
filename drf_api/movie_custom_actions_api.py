from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response


class MovieCustomActionsView(GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=False, methods=['get'])
    def classic_movies(self, request):
        classic_movies = Movie.objects.all().order_by('-id')

        page = self.paginate_queryset(classic_movies)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(classic_movies, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def movie_details(self, request, pk=None):
        movie = self.get_object()
        serializer = self.serializer_class(movie)
        return Response(serializer.data)
