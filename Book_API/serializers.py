from rest_framework import serializers
from .models import Books, User, Carousel,Expenses,Sales
# from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)
        # extra_kwargs = {'password':{'write_only':True, 'required':True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     Token.objects.create(user=user)
    #     return user
class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


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
