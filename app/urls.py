from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views.user_views import UserView
from app.views.post_views import PostView
from app.views.vote_views import VoteView

router = DefaultRouter()
router.register(r"posts", PostView, basename="post")

urlpatterns = [
    path("users/", UserView.as_view(), name="users"),
    # path("posts/", PostView.as_view(), name="posts"),
    path("", include(router.urls)),  # This registers the ViewSet routes
    path("votes/", VoteView.as_view(), name="votes"),
]
