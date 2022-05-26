from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    fields = ('id', 'tex', 'author', 'image', 'group')
    model = Post
