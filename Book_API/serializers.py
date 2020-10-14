from rest_framework import serializers
from .models import Books, User, Carousel
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

#class Search_dataSerializer(serializers.ModelSerializer):

#pass
