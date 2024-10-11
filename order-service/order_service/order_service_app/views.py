import requests
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, status, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Orders
from .serializers import OrderSerializer


class OrderAPIView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if request.user.is_staff:
            queryset = self.queryset.all()
        else:
            queryset = self.queryset.filter(owner=request.user)

        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        jwt_token = request.headers.get('Authorization')
        books_string = request.data.get('books', '')
        if not books_string:
            return Response({'error': 'Books parameter is required.'}, status=400)
        try:
            response = requests.get(
                f'http://book-service:8000/books/?books={books_string}',
                headers={'Authorization': jwt_token}
            )
            response.raise_for_status()
            books_data = response.json()
        except requests.RequestException as e:
            return Response({'error': 'Failed to fetch books'}, status=500)

        order = Orders.objects.create(
            owner=request.user,
            books=books_data
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
