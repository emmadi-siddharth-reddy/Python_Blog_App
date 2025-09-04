from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "index.html",{"posts":posts})

# def all_posts(request):
#     posts = Post.objects.all()
#     return render(posts)