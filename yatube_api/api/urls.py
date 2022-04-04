from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='PostsView')
router.register('groups', GroupViewSet, basename='GroupsView')
router.register('follow', FollowViewSet, basename='FollowView')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='CommentView')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
