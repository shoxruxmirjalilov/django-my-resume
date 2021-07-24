from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models  import Q
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.

class PostIndexView(ListView):
    model = Post
    template_name = 'index.html'
    queryset=Post.objects.all()
    context_object_name = 'post'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'    



class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains=query).all()

 

