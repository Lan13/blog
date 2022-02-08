from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blogs.models import BlogPost
from .forms import CommentForm
from .models import Comment
import markdown
from django.http import Http404
# Create your views here.

@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=comment.blog.id)

    context = {'comment': comment, 'form': form}
    return render(request, 'comments/edit_comment.html', context)