from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    template_name = "list.html"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(is_deleted=False)

        return render(request, self.template_name, {"posts": posts})