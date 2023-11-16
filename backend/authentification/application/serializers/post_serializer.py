from rest_framework import serializers
from authentification.application.serializers.user_serializer import UserSerializer


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=255)
    date_posted = serializers.DateTimeField(read_only=True)
    author = UserSerializer()

    def create(self, validated_data):
        self.author = serializers.IntegerField(read_only=True)
