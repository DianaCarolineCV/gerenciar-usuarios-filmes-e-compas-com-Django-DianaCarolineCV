from rest_framework import serializers
from .models import Movie, Rating, MovieOrder
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10,
        allow_null=True,
        default=None,
    )
    rating = serializers.ChoiceField(
        allow_null=True,
        choices=Rating.choices,
        default=Rating.DEFAULT,
    )
    synopsis = serializers.CharField(
        allow_null=True,
        default=None,
    )
    added_by = serializers.CharField(
        read_only=True,
        allow_null=True,
        default=None,
    )

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        added_by_obj = movie.user.email
        movie.added_by = added_by_obj
        movie.save()
        return movie


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_title(self, obj: Movie):
        return obj.movie.title

    def get_buyed_by(self, obj: User):
        return obj.user.email

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
