from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from posts.models import Post

# Create your views here.

def home(request):
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request,'posts/index.html', {'posts':all_posts})

def post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        raise Http404()
    return render(request, 'posts/post.html', {'post_dict':post})

def global_view(request):
    return render(request, 'lala.html')