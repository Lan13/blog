from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
import markdown
from django.contrib.auth.models import User
from comments.models import Comment
from comments.forms import CommentForm
from django.core.paginator import Paginator
from users.models import Profile
# Create your views here.


def index(request):
    return render(request, 'blogs/index.html')



def blogs(request):
    blogs = BlogPost.objects.order_by('-date_added')
    # 这里开始修改
    paginator = Paginator(blogs, 4)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    for blog in blogs:
        if len(f"{blog.text}") >= 50:
            blog.text = f"{blog.text[:50]}......"
        blog.text = markdown.markdown(blog.text, extensions=['markdown.extensions.extra',
                                                             'markdown.extensions.codehilite',
                                                             'markdown.extensions.toc',
                                                             'markdown.extensions.tables'])
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)



def blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    blog.text = markdown.markdown(blog.text, extensions=['markdown.extensions.extra',
                                              'markdown.extensions.codehilite',
                                              'markdown.extensions.toc',
                                              'markdown.extensions.tables'])
    comments = Comment.objects.filter(blog_id=blog_id)
    for comment in comments:
        comment.text = markdown.markdown(comment.text, extensions=['markdown.extensions.extra',
                                                                     'markdown.extensions.codehilite',
                                                                     'markdown.extensions.toc',
                                                                     'markdown.extensions.tables'])
    if request.method != 'POST':
        comment_form = CommentForm()
    else:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.owner = request.user
            new_comment.save()
            return redirect('blogs:blog', blog_id=blog.id)
    if blog.owner == request.user:
        auth = True
    else:
        auth = False
    context = {'blog': blog, 'auth': auth, 'comments': comments, 'form': comment_form}
    return render(request, 'blogs/blog.html', context)


@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:blog', blog_id=new_blog.id)
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    if blog.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

def homepage(request, user_id):
    user = User.objects.filter(id=user_id) # 这是一个Queryset 所以要使用切片
    blogs = BlogPost.objects.filter(owner=user[0]).order_by('-date_added')
    profile = Profile.objects.get(user_id=user_id)

    paginator = Paginator(blogs, 1)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    for blog in blogs:
        if len(f"{blog.text}") >= 50:
            blog.text = f"{blog.text[:50]}......"
        blog.text = markdown.markdown(blog.text, extensions=['markdown.extensions.extra',
                                                                   'markdown.extensions.codehilite',
                                                                   'markdown.extensions.toc',
                                                                   'markdown.extensions.tables'])
    visit_user = user[0]
    context = {'blogs': blogs, 'visit_user': visit_user, 'profile': profile}
    return render(request, 'blogs/homepage.html', context)