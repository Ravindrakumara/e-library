from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.generics import ListAPIView
from .models import Books, User, Carousel,Category
from .serializers import BookSerializer, UserSerializer, CarouselSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    page_size = 1000
    page_size_query_param = 'page_size'


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class BookList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['isbn','book','language','publisher','edition']  # this for search any book , 'book', 'language', 'category','publisher', 'edition'


