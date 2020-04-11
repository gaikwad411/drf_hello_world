from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    poster = models.ImageField(null=True, upload_to='movie_posters')
