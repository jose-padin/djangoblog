from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView

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

    # TODO: use a form for this
    def post(self, request, *args, **kwargs):
        author = request.user

        if not author.is_authenticated:
            return redirect("posts:add")
        
        obj = Post()
        obj.title = request.POST["title"]
        obj.text = request.POST["text"]
        obj.author = request.user
        obj.image = request.FILES["image"]
        obj.save()

        return redirect("post:list")


class PostDetailView(DetailView):
    template_name = "detail.html"
    pk_url_kwarg = "post_id"
    queryset = Post.objects.filter(is_deleted=False)
