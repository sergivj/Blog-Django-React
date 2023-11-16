import json

from rest_framework import serializers
from authentification.models import User, Post


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        mail_exists = User.objects.filter(email=validated_data['email']).exists()
        user_exists = User.objects.filter(username=validated_data['username']).exists()
        if user_exists or mail_exists:
            return {'error': 'El usuario ya existe'}

        user = User().create_new_user(
            validated_data['username'],
            validated_data['first_name'],
            validated_data['last_name'],
            validated_data['email'],
            validated_data['password']
        )

        return user


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class PostsSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'date_posted', 'author')


class NewEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
