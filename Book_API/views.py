from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.generics import ListAPIView
from .models import Books, User, Carousel,Category,Sales,Expenses
from .serializers import BookSerializer, UserSerializer, CarouselSerializer,ExpenseSerializers,SalesSerializers
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from knox.auth import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    permission_class = [
        permissions.IsAuthenticated
    ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        return self.request.user.Book_API.all()
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    page_size = 1000
    page_size_query_param = 'page_size'
# this permission alowed to Adminuser and most login
#     def get_permissions(self):
#         if self.request.method in ['PUT', 'DELETE']:
#             return [permissions.IsAdminUser()]
#         return [permissions.IsAuthenticated()]
# ?
#     def get_permissions(self):
#         if self.request.method == 'DELETE':
#             return [permission() for permission in (AllowAny,)]
#         return super(BookViewSet, self).get_permissions()

class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer

class BookList(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['isbn','book','language','publisher','edition']  # this for search any book , 'book', 'language', 'category','publisher', 'edition'

#========= 2020-12-30 =============

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpenseSerializers
    pass

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializers
    pass

