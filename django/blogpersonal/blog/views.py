from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.
def posts(request):
    blogs=Post.objects.all()
    return HttpResponse(blogs)


def post(request,id):
    blog=Post.objects.get(id=id)
    content=f'{blog.title} - {blog.desc}'
    return HttpResponse(content)