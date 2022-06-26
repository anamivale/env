from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
from django.views import generic


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'


class PostCreateView(generic.CreateView):
    model: Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    template_name = 'post_form.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'


class PostUpdateView(generic.UpdateView):
    model: Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    template_name = 'post_form.html'


class PostDeleteView(generic.DeleteView):
    model: Post
    fields = "__all__"
    success_url = reverse_lazy("blog: all")
    template_name = 'post_confirm_delete.html'
