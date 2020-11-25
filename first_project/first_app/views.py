from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def userlist(request):
    users = User.objects.all()
    return HttpResponse(users)

def bloglist(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'first_app/blog.html',context)

def postlist(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'first_app/post.html', context)