from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer , LoginSerializer ,UserListSerializer ,UserUpdateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Login successful",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "role": user.role,
                "email": user.email,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersListView(APIView):
    def get(self, request):
        user = request.user


        if not user.is_authenticated:
            return Response({"detail": "Authentication required."},
                            status=status.HTTP_401_UNAUTHORIZED)

        if user.role != "admin":
            return Response({"detail": "Only admin can view all users."},
                            status=status.HTTP_403_FORBIDDEN)

        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailView(APIView):

    def get(self, request, user_id):
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Login required."},
                            status=status.HTTP_401_UNAUTHORIZED)

        if user.id != user_id and user.role != "admin":
            return Response({"detail": "Permission denied."},
                            status=status.HTTP_403_FORBIDDEN)
        target_user = User.objects.get(id=user_id)
        serializer = UserUpdateSerializer(target_user)
        return Response(serializer.data, status=200)

    def put(self, request, user_id):
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Login required."},
                            status=status.HTTP_401_UNAUTHORIZED)


        if user.id != user_id and user.role != "admin":
            return Response({"detail": "Permission denied."},
                            status=status.HTTP_403_FORBIDDEN)

        target_user = User.objects.get(id=user_id)
        serializer = UserUpdateSerializer(target_user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully"})

        return Response(serializer.errors, status=400)

    def delete(self, request, user_id):
        user = request.user

        if not user.is_authenticated:
            return Response({"detail": "Login required."},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Delete = only admin!
        if user.role != "admin":
            return Response({"detail": "Only admin can delete users."},
                            status=status.HTTP_403_FORBIDDEN)

        target_user = User.objects.get(id=user_id)
        target_user.delete()
        return Response({"message": "User deleted."}, status=200)