from .forms import EditPost
from .models import Post
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


class Posts(ListView):
    template_name = "pdown/list.html"
    model = Post
    context_object_name = "posts"


class CreatePost(CreateView):
    form_class = EditPost
    template_name = "pdown/edit.html"
    success_url = '/'


class UpdatePost(UpdateView):
    form_class = EditPost
    model = Post
    pk_url_kwarg = "id"
    template_name = "pdown/update.html"
    success_url = '/'

