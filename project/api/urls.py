from rest_framework import routers
from django.urls import path, include
from books.viewsets import AuthorViewSet, BookViewSet, PublisherViewSet
from .viewsets import LoginView


router = routers.DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register('publisher', PublisherViewSet, basename='publisher')
router.register('books', BookViewSet, basename='books')


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('', include(router.urls)),
]
