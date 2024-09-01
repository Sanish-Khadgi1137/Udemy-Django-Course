from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    # post/my-first-post; here "my-first-post" is slug(dymanic segment); slug-format contains only letters number and dash
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]
