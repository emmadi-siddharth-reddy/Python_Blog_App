from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "index.html",{"posts":posts})

def all_posts(request):
    posts = Post.objects.all()
    return JsonResponse({"posts": list(posts.values())})

def post_detail(request, id):
    try:
        post = Post.objects.values("id", "title", "content").get(id=id)
        return JsonResponse(post, safe=False)  # now it’s dict, not model
    except Post.DoesNotExist:
        return HttpResponse("Post not found", status=404)