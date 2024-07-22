from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.

def main(req):
    posts = Post.objects.all()
    ctx = {
        'posts': posts
    }
    return render(req,'main.html',ctx)

def create(req):
    if req.method == "GET":
        form = PostForm()
        ctx = {
            'form': form
        }
        return render(req, 'create.html',ctx)
    
    form = PostForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
        return redirect("posts:main")
    else:
        ctx = {
            'form': form
        }
        return render(req, 'create.html', ctx)


def detail(req,pk):
    post=Post.objects.get(id=pk)
    ctx = {
        "post": post
    }
    return render(req, 'detail.html', ctx)

def like(req):
    req = json.loads(req.body)
    post_id = req['id']

    post = Post.objects.get(id=post_id)

    if button_type == 'like':
        button_type = 'unlike'
    else:
        button_type = 'like'
        
    post.save()
    return JsonResponse({'id': post_id , 'type': button_type})

def comment(req, pk):
    post = Post.objects.get(id=pk)
    if req.method == 'POST':
        content = req.POST.get('content')
        comment = Comment.objects.create(post=post, content=content)
        return JsonResponse({'comment_id': comment.id, 'content': comment.content})

def comment_delete(req, pk):
    comment = Post.objects.get(id=pk)
    comment.delete()
    return JsonResponse()