from django.urls import path
from .views import all_posts, post_detail

app_name = "blog"

urlpatterns = [
    path("", all_posts, name="posts"),
    path("<int:post_id>", post_detail, name="post_detail"),
]
