from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import CreateView, DetailView, ListView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    template_name = "list.html"

    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(
            pub_date__lte=timezone.now(),
            is_deleted=False,
        )
        return render(request, self.template_name, {"posts": posts})

    def post(self, request, *args, **kwargs):
        search_tags = request.POST["search"]

        posts = Post.objects.filter(
            pub_date__lte=timezone.now(),
            tags__name__icontains=search_tags,
            is_deleted=False,
        )

        return render(
            request,
            self.template_name,
            {
                "posts": posts,
                "method": "post"
            },
        )

class PostCreateView(CreateView):
    model = Post
    fields = ("title", "text", "tags", "image")
    template_name = "form.html"
    form = PostForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        author = request.user

        if not author.is_authenticated:
            return redirect("posts:add")
        
        form = self.form(request.POST, request.FILES, author=author)

        if form.is_valid():
            form.save()
            return redirect("post:list")

        return render(request, self.template_name, {"form": form, "errors": form.errors})


class PostDetailView(DetailView):
    template_name = "detail.html"
    pk_url_kwarg = "post_id"
    queryset = Post.objects.filter(is_deleted=False)
