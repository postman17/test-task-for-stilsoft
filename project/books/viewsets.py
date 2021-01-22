from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Publisher, Book
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer
from .permissions import IsAdminOrReadOnly


class AuthorViewSet(ModelViewSet):
    """Author viewset."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser, ]


class PublisherViewSet(ModelViewSet):
    """Publisher viewset."""

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = [IsAdminUser, ]


class BookViewSet(ModelViewSet):
    """Book viewset."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, OrderingFilter, ]
    filterset_fields = ['title', ]
    ordering_fields = '__all__'
