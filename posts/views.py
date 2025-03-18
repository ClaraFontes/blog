from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from posts.models import Post

# Create your views here.

posts = [
    {
        'id': 1,
        'title': 'Vamos explorar Python',
        'content': 'Python é uma linguagem de programação de alto nível, interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.'
    },

    {
        'id': 2,
        'title': 'Vamos explorar JavaScript',
        'content': 'JavaScript é uma linguagem de programação usada por desenvolvedores para fazer páginas interativas da Internet.'
    },

    {
        'id': 3,
        'title': 'Django é o melhor framework!',
        'content': 'Django é usado por quase todas as maiores empresas tech como facebook, google, youtube, instagram, etc.'
    },
]

def home(request):
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request,'posts/index.html', {'posts':all_posts})

def post(request, id):
    valid_id = False
    for post in posts:
        if post['id'] == id:
            post_dict = post
            valid_id = True
            break

    if valid_id:
        return render(request, 'posts/post.html', {'post_dict':post_dict})
    else:
        # return HttpResponseNotFound("Este post não está disponível...")
        raise Http404()

def global_view(request):
    return render(request, 'lala.html')