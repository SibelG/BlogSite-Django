from django.shortcuts import render,HttpResponse,get_object_or_404
# Create your views here.
from .models import Blog, Category


def home(request):
    #posts = Post.objects.all()
    context= {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, 'post/home.html', context)

def post_index(request):
    #posts = Post.objects.all()
    context= {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, 'post/index.html', context)


def post_detail(request,id):
    blog = Blog.objects.get(id=id)

    #selectedBlocks=[blog for blog in blogs if blog["id"]==id][0]
    return render(request,'post/detail.html', {"blog":blog})

def blogs_by_category(request,id):
    context = {
        "blogs": Category.objects.get(id=id).blog_set.filter(is_active=True),
        #"blogs": Blog.objects.filter(is_active=True, category__id=id),
        "categories": Category.objects.all(),
        "selected_category":id
    }
    return render(request, 'post/index.html', context)

def post_create(request):
    return HttpResponse("create")

def post_update(request):
    return HttpResponse("update")

def post_delete(request):
    return HttpResponse("delete")



