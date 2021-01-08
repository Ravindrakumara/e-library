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

# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from knox.auth import TokenAuthentication

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

