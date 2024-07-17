from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def main(req):
    sort_option = req.GET.get('sort','latest')
    if sort_option == 'latest':
        posts = Post.objects.all().order_by('-pk')  # 최신순 (pk순)
    elif sort_option == 'name':
        posts = Post.objects.all().order_by('title')  # 이름순
    elif sort_option == 'interest':
        posts = Post.objects.all().order_by('-interest')  # 관심도순
    else:
        posts = Post.objects.all()
    ctx = {
        'posts': posts,
        'sort_option': sort_option  # 현재 선택된 정렬 옵션을 템플릿에 전달
    }
    return render(req, 'posts/list.html',ctx)

def create(req):
    if req.method == "GET":
        form = PostForm()
        ctx = {
            'form': form
        }
        return render(req, 'posts/create.html',ctx)
    form = PostForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
    return redirect("posts:main") 

def detail(req, pk):
  post = Post.objects.get(id=pk)
  ctx = {'post':post}
  return render(req,'posts/detail.html',ctx)

def delete(req, pk):
    Post.objects.get(id=pk).delete()
    return redirect('posts:main')

def update(req,pk):
    post = Post.objects.get(id=pk)
    if req.method == "GET":
        form = PostForm(instance=post)
        ctx  = {
            'form': form,
            'pk':pk
        }
        return render(req, 'posts/update.html',ctx)
    form = PostForm(req.POST, req.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect("posts:detail",pk) 

def update_interest(request, pk, btn):
    post = Post.objects.get(id=pk)
    if btn == 'increase':
        post.interest += 1
    elif btn == 'decrease' and post.interest > 0:
        post.interest -= 1
    post.save()
    return HttpResponse(post.interest)