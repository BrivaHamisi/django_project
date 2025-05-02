from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse("Hello, world. You're at the blog home.")

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    # return HttpResponse("This is the about page.")