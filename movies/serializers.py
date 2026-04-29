from rest_framework import serializers

from .models import Movie
from .models import  Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
        ]


class MovieSerializer(serializers.ModelSerializer):

    genres_detail = GenreSerializer(
        source="genres",
        many=True,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "release_year",

            "genres",
            "genres_detail",
        ]