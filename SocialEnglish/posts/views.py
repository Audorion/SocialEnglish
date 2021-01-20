from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Group
from django.views.generic import CreateView
from .forms import PostForm


def index(request):
    latest = Post.objects.order_by('-pub_date')[:11]
    return render(request, "index.html", {"posts": latest})


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


class PostNew(CreateView):
    form_class = PostForm
    success_url = "/group"
    template_name = "new_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super(PostNew, self).form_valid(form)