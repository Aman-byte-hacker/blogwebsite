from django.shortcuts import render
from .models import Blog
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def blog(request):
    blogs=Blog.objects.all()
    content={
        'blogs':blogs
    }
    return render(request,"blog.html",content)

def search(request):
    query=request.GET['query']
    if len(query)>40:
        return HttpResponse("We Don't Support a Lot of words to Search It Is Beyond Our Security Purposes!🤐")
    blogs=Blog.objects.filter(name__icontains=query)
    content={
        'blogs':blogs
    }
    return render(request,"search.html",content)   
def about(request):
    return render(request,"about.html")
