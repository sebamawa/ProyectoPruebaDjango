from django.shortcuts import render, get_object_or_404
from .models import Post, PostForm
from django.views.generic import CreateView, ListView

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status='published')
    #print(posts)

    return render(request, 'posts/post_list.html', {'posts': posts})

# ListView (Class-based view)
class PostListView(ListView):
    model = Post
    # template_name = 'post/post_list.html'

    # fltra los registros pasados al template
    def get_queryset(self):
        return Post.objects.filter(status='published')

# CreateView (Class-based view)
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'
