from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from Book_API.views import BookList
from .views import  BookViewSet, CarouselViewSet, ExpenseViewSet, SalesViewSet

router = routers.DefaultRouter()

router.register('Book', BookViewSet)
router.register('Banner', CarouselViewSet)
router.register('Expense', ExpenseViewSet)
router.register('Sale', SalesViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('books/', BookList.as_view())
]

