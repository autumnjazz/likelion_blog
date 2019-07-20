from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blogapp/home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogapp/detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'blogapp/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

    
def about(request):
    return render(request, 'blogapp/about.html')


    
def delete(request, blog_id):
    post = Blog.objects.get(id=blog_id)
    post.delete() # delete는 save를 내장하고 있다.
    return redirect("home")

def edit(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    if request.method == "POST":
        blog_detail.title = request.POST['title']
        blog_detail.body = request.POST['body']
        blog_detail.save()
        return redirect('home')
    
    else:
        return render(request, 'blogapp/edit.html', {'blog': blog_detail})

def comment_create(request,blog_id):
    if request.method == "POST":
        blog = Blog.objects.get(id=blog_id)
        comment = Comment(blog = blog) #앞의 post는 Comment()의 변수
        if request.POST['content'] :
            comment.content = request.POST['content']
            comment.save()

        return redirect('detail', blog_id)
    else:
        pass


def comment_delete(request, blog_id, cmt_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    cmt = get_object_or_404(Comment, pk = cmt_id)
    cmt.delete()
    return redirect('detail', blog_id)