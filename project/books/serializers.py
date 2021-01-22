from rest_framework import serializers
from .models import Author, Publisher, Book


class AuthorSerializer(serializers.ModelSerializer):
    """Author serializer."""

    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    """Publisher serializer."""

    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    """Book serializer."""

    class Meta:
        model = Book
        fields = '__all__'
