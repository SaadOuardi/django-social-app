from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views.user_views import UserRegisterView
from app.views.post_views import PostViewSet
from app.views.vote_views import VoteView
from app.views.auth_views import urlpatterns as auth_urls
from app.views.home_views import HomeView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="posts")

urlpatterns = [
    path('/yo', HomeView.as_view(), name="home"),
    path('auth/', include(auth_urls)),
    path('users/register/', UserRegisterView.as_view(), name='register'),
    path('votes/<uuid:post_id>/', VoteView.as_view(), name="votes"),
    path('', include(router.urls)),
]