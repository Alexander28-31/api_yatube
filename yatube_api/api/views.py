from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticated, IsAuthenticatedOrReadOnly)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(
            Post, pk=self.kwargs.get('post_pk'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post, pk=self.kwargs.get('post_pk'))
        serializer.save(author=self.request.user, post=post)
