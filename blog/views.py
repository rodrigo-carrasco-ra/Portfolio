from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post_id=get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post_id})


#getobjet_or_404 is a shortcut to get an object or return a 404 error if it doesn't exist