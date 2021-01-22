from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'title',
    )
    list_display = (
        'id',
        'title',
        'created_at',
    )


@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'title',
    )
    list_display = (
        'id',
        'title',
        'created_at',
    )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'title',
        'description',
    )
    list_display = (
        'id',
        'title',
        'description',
        'publisher',
        'get_authors',
        'created_at',
    )

    def get_authors(self, book):
        return ', '.join([author.title for author in book.authors.all()])
    get_authors.short_description = _('Authors')
