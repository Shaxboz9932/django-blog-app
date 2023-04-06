from django.views.generic import (ListView,
                                  DetailView,
                                  UpdateView,
                                  CreateView,
                                  DeleteView,
                                  )

from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    template_name = 'home.html'
    model = Post

class BlogDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post

class BlogEditView(UpdateView):
    template_name = 'post_edit.html'
    model = Post
    fields = ['title', 'body']
    # success_url = reverse_lazy('home')

class BlogCreateView(CreateView):
    template_name = 'post_new.html'
    model = Post
    fields = ['title', 'author', 'body']

class BlogDeleteView(DeleteView):
    template_name = 'post_delete.html'
    model = Post
    success_url = reverse_lazy('home')



