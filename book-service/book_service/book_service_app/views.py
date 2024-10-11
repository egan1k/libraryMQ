from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Category
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BooksAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = (IsAuthenticated, )
    pagination_class = BooksAPIListPagination
    # authentication_classes = (TokenAuthentication, SessionAuthentication)

    @method_decorator(cache_page(20))
    @method_decorator(vary_on_headers('Authorization'))
    def list(self, request, *args, **kwargs):
        filter_kwargs = {}
        books_cache_name = 'books_cache'
        author_param_name = 'author'
        category_param_name = 'cat'
        books_param_name = 'books'

        author = request.query_params.get(author_param_name, None)
        cat = request.query_params.get(category_param_name, None)
        books = request.query_params.get(books_param_name, None)

        if books:
            books_ids = books.split(',')
            queryset = self.get_queryset().filter(pk__in=books_ids)
            return Response(self.serializer_class(queryset, many=True).data)

        if author:
            filter_kwargs[author_param_name] = author
        if cat:
            filter_kwargs[category_param_name] = cat

        queryset = self.get_queryset().filter(**filter_kwargs)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)


