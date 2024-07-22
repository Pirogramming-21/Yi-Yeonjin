from django.shortcuts import render, redirect
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
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


def detail(req, pk):
    post = Post.objects.get(id=pk)
    liked = False
    liked = Like.objects.filter(post=post).exists()
    ctx = {
        "post": post,
        "liked": liked
    }
    return render(req, 'detail.html', ctx)

@csrf_exempt
def like(req):
    data = json.loads(req.body)
    post_id = data['id']

    post = Post.objects.get(id=post_id)

    user_liked = Like.objects.filter(post=post).exists()

    if user_liked:
        Like.objects.filter(post=post).delete()
        post.like -= 1
        liked = False
    else:
        Like.objects.create(post=post)
        post.like += 1
        liked = True

    post.save()

    return JsonResponse({'id': post_id, 'likes': post.like, 'liked': liked})


@csrf_exempt
def comment(req, pk):
    post = Post.objects.get(id=pk)
    if req.method == 'POST':
        content = req.POST.get('content')
        comment = Comment.objects.create(post=post, content=content)
        return JsonResponse({'comment_id': comment.id, 'content': comment.content})

@csrf_exempt
def comment_delete(req, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return JsonResponse({'success': True})