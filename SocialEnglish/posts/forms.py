from .models import Post
from django.forms import ModelForm
from django.contrib.auth import get_user_model

User = get_user_model()


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
