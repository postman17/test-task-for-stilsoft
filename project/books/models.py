from django.db import models


class Author(models.Model):
    """Represent authors."""

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'books__authors'
        indexes = (
            models.Index(fields=['title']),
            models.Index(fields=['created_at']),
        )

    def __str__(self):
        return self.title


class Publisher(models.Model):
    """Represent a publisher of books."""

    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'books__publishers'
        indexes = (
            models.Index(fields=['title']),
            models.Index(fields=['created_at']),
        )

    def __str__(self):
        return self.title


class Book(models.Model):
    """Represent books."""

    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    publisher = models.ForeignKey('Publisher', related_name='books', on_delete=models.CASCADE, null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books_written', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'books__books'
        indexes = (
            models.Index(fields=['title']),
            models.Index(fields=['created_at']),
        )

    def __str__(self):
        return self.title
