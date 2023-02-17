from rest_framework import permissions
from movies.models import Movie


class MovieOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, movie: Movie) -> bool:
        return movie.user == request.user
