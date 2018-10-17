from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from blog.models import Comment, Post
from blog.forms import CommentForm, PostForm


# TODO watch more aboutview
class AboutView (TemplateView):
    template_name = 'about.html'


# Create your views here.
class PostListView (ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte = timezone.now()).order_by('-published_date')


class DetailPostView (DetailView):
    model = Post


class CreatePostView (LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    form_class= PostForm
    model = Post


class DeletePostView (LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Post
    success_url = reverse_lazy ('post_list')


class DraftListView (LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('create_data')