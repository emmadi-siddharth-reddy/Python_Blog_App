from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .form import PostForm
from .models import Post

# Create your views here.
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
    