from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
import datetime


# Create your views here.


def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {'posts': posts})

def newpost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('myblog:feed')
    else:
        form = PostForm()
    return render(request, 'newpost.html', {'form': form})

def post_info(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_info.html', {'post': post})