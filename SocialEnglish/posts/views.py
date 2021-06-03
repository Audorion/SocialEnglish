from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from transliterate import translit


from .models import Post
from django.views.generic import CreateView, ListView, DetailView
from django.core.paginator import Paginator
from .forms import PostForm
from django.urls import reverse_lazy


# def index(request):
#    post_list = Post.objects.all()
#    paginator = Paginator(post_list, 10)
#    page_number = request.GET.get('page')
#    page = paginator.get_page(page_number)
#    return render(request, "index3.html", {"page": page,
#                                           "paginator": paginator})


class PostList(ListView):
    model = Post
    context_object_name = 'post'
    template_name = 'index3.html'
    paginate_by = 5


    def get_queryset(self):
        return Post.objects.order_by('-pub_date')


class ShowPost(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


#def profile(request, username):
#    post_list = Post.objects.filter(username=username).all()
#    paginator = Paginator(post_list, 10)
#    page_number = request.GET.get('page')
#    page = paginator.get_page(page_number)
#    count = Post.objects.filter(username=username).length()
#    return render(request, 'profile.html', {"page": page, "paginator": paginator, "username": username, "count": count})


@login_required()
def post_edit(request, username, post_id):
    post_list = Post.objects.filter(username=username).all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    count = Post.objects.filter(username=username).length()
    # тут тело функции. Не забудьте проверить,
    # что текущий пользователь — это автор записи.
    # В качестве шаблона страницы редактирования укажите шаблон создания новой записи
    # который вы создали раньше (вы могли назвать шаблон иначе)
    return render(request, 'new_post.html',
                  {"page": page, "paginator": paginator, "username": username, "count": count})


class PostNew(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('index')
    template_name = "new_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.slug = slugify(translit(post.title, language_code='ru', reversed=True))
        post.save()
        return super(PostNew, self).form_valid(form)
