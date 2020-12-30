from rest_framework import serializers
from .models import Books, User, Carousel,Expenses,Sales
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None)

    class Meta:
        model = Books
        fields = ('id','isbn','book','language','category','description','publisher','pub_date','pages','note','edition','image','create_date')
        read_only_fields = ['image']


class CarouselSerializer(serializers.ModelSerializer):
    banner = serializers.ImageField(max_length=None)
    class Meta:
        model = Carousel
        fields = ('headline', 'banner')
        read_only_fields = ['banner']

# This serializer added to 30-12-2020

class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ("id","book","transport","transport_cost","purchase_price","exchange_rates","sale_price","total_book_cost","quantity","date","create_date")
    pass

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ("id","book","sale_price","quantity","total","stock")
    pass
#class Search_dataSerializer(serializers.ModelSerializer):

#pass
