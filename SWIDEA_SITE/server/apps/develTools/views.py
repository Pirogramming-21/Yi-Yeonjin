from django.shortcuts import render, redirect
from .models import DevelTool
from apps.posts.models import Post
from .forms import DevelToolForm

# Create your views here.
def list(req):
    tools = DevelTool.objects.all()
    ctx = {
        'tools': tools
    }
    return render(req, 'develtools/list.html', ctx)

def create(req):
    if req.method == "GET":
        form = DevelToolForm()
        ctx = {
            'form': form
        }
        return render(req, 'develtools/create.html',ctx)
    form = DevelToolForm(req.POST)
    if form.is_valid():
        form.save()
    return redirect("develtools:list")

def detail(req, pk):
  tool = DevelTool.objects.get(id=pk)
  related_posts = Post.objects.filter(devtool=tool)
  ctx = {
        'tool':tool,
        'related_posts': related_posts
    }
  return render(req,'develtools/detail.html',ctx)

def delete(req, pk):
    DevelTool.objects.get(id=pk).delete()
    return redirect("develtools:list")

def update(req, pk):
    user = DevelTool.objects.get(id=pk)
    if req.method == "GET":
        form = DevelToolForm(instance=user)
        ctx  = {
            'form': form,
            'pk':pk
        }
        return render(req, 'develtools/update.html', ctx)
    form = DevelToolForm(req.POST, instance=user)
    if form.is_valid():
        form.save()
    return redirect("develtools:detail",pk) #detail 페이지는 pk가 필요