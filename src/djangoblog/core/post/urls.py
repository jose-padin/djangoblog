from django.urls import re_path

from .views import PostCreateView, PostDetailView, PostListView

urlpatterns = [
    re_path(r"^$", PostListView.as_view(), name="list"),
    re_path(r"^add$", PostCreateView.as_view(), name="add"),
    re_path(r"^(?P<post_id>\d+$)", PostDetailView.as_view(), name="detail"),
]
