from rest_framework.views import APIView, Request, Response, status
from .serializer import RegisterUserSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsEmployee
from django.shortcuts import get_object_or_404


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = RegisterUserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        user_serialized = RegisterUserSerializer(user, data=request.data, partial=True)
        user_serialized.is_valid(raise_exception=True)
        user_serialized.save()

        return Response(user_serialized.data, status=status.HTTP_200_OK)
