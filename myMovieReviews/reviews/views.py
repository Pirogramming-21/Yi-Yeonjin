from django.shortcuts import render
from .models import Post

# Create your views here.
def review_list(request):
    reviews = Post.objects.all() 
    context = {
        "reviews": reviews
    }
    return render(request, 'review_list.html', context) 