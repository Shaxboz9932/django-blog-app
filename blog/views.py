from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    template_name = 'home.html'
    model = Post


