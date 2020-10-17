from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from Book_API.views import BookList
from .views import UserViewSet, BookViewSet, CarouselViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('Book', BookViewSet)
router.register('Banner', CarouselViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('books/', BookList.as_view())
]

