from django.urls import include, path
from rest_framework import routers

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowList

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowList, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
