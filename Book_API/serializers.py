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
        fields = '__all__'
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
        fields = '__all__'
    pass

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
    pass
#class Search_dataSerializer(serializers.ModelSerializer):

#pass
