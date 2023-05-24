from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        depth = 1
        fields = ['id', 'title', 'body', 'author']
    
    def get_author(self, obj):
        return obj.author.username
