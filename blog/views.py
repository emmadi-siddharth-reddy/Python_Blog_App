from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import generics

from .serializer import PostSerializer

from .form import PostForm
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "index.html",{"posts":posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_details.html", {'post':post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,  "Post created successfully!")
            return redirect("post_detail",id=post.id)
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})
    
    
def post_edit(request, id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id = post.id)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'post_form.html', {'form':form})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')


class PostListAPI(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer