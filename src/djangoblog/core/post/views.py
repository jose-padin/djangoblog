from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView

from .models import Post


class PostListView(ListView):
    template_name = "list.html"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(is_deleted=False)

        return render(request, self.template_name, {"posts": posts})


class PostCreateView(CreateView):
    model = Post
    fields = ("title", "text", "tags", "image")
    template_name = "form.html"

    def post(self, request, *args, **kwargs):
        obj = Post()
        obj.title = request.POST["title"]
        obj.text = request.POST["text"]
        obj.image = request.POST["image"]
        obj.author = request.user
        obj.save()
        return redirect("post:list")