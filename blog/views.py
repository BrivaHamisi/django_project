from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2023'
    },
    {
        'author': 'Alice Johnson',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 29, 2023'
    }]

# Create your views here.
def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse("Hello, world. You're at the blog home.")

def about(request):
    return render(request, 'blog/about.html')
    # return HttpResponse("This is the about page.")