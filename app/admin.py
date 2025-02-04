from django.contrib import admin
from app.models.user import User
from app.models.post import Post
from app.models.vote import Vote

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Vote)
