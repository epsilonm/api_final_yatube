from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Group
from .permissions import IsAuthorOrReadOnly
from .serializers import (PostSerializer, GroupSerializer,
                          CommentSerializer, FollowSerializer)


class YatubeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class PostViewSet(YatubeViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(YatubeViewSet):
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return self.get_post().comments.all()


class FollowViewSet(YatubeViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    search_fields = ('following__username',)
    ordering_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
