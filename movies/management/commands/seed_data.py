from django.core.management.base import BaseCommand

from movies.models import Movie, Genre


class Command(BaseCommand):
    help = "Carga data inicial de géneros y películas"

    def handle(self, *args, **options):
        action, _ = Genre.objects.get_or_create(name="Acción")
        comedy, _ = Genre.objects.get_or_create(name="Comedia")
        drama, _ = Genre.objects.get_or_create(name="Drama")
        sci_fi, _ = Genre.objects.get_or_create(name="Ciencia Ficción")

        interstellar, _ = Movie.objects.get_or_create(
            title="Interstellar",
            defaults={
                "description": "Película de ciencia ficción sobre viajes espaciales.",
                "release_year": 2014,
            },
        )

        inception, _ = Movie.objects.get_or_create(
            title="Inception",
            defaults={
                "description": "Película sobre sueños dentro de sueños.",
                "release_year": 2010,
            },
        )

        joker, _ = Movie.objects.get_or_create(
            title="Joker",
            defaults={
                "description": "Historia dramática del origen del Joker.",
                "release_year": 2019,
            },
        )

        spider_man, _ = Movie.objects.get_or_create(
            title="Spider-Man",
            defaults={
                "description": "Película de superhéroes y acción.",
                "release_year": 2002,
            },
        )

        interstellar.genres.add(sci_fi, drama)
        inception.genres.add(sci_fi, action)
        joker.genres.add(drama)
        spider_man.genres.add(action)

        self.stdout.write(
            self.style.SUCCESS("Data inicial cargada correctamente.")
        )