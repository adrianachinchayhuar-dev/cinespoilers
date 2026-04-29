from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()

    genres = models.ManyToManyField(
        Genre,
        related_name="movies",
        blank=True
    )

    def __str__(self):
        return self.title