from django.db import models


class Rating(models.TextChoices):
    DEFAULT = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        null=True,
        choices=Rating.choices,
        default=Rating.DEFAULT,
    )
    synopsis = models.TextField(
        null=True,
        default=None,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movie",
        null=True,
    )


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_orders",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_orders",
    )

    buyed_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
