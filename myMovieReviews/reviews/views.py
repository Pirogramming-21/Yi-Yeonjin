from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def review_list(request):
    reviews = Post.objects.all() 
    context = {
        "reviews": reviews
    }
    return render(request, 'review_list.html', context) 

def review_create(request):
    if request.method == "POST":
        Post.objects.create( 
            title=request.POST["title"],
            release_year=request.POST["release_year"],
            genre=request.POST["genre"],
            rating=request.POST["rating"],
            running_time=request.POST["running_time"],
            review=request.POST["review"],
            director=request.POST["director"],
            actors=request.POST["actors"]
        )
        return redirect("/reviews")
    return render(request, 'review_create.html')

def review_detail(request,pk):
    review=Post.objects.get(id=pk)
    context = {
        "review": review,
    }
    return render(request, 'review_detail.html', context)

def review_update(request, pk):
    review=Post.objects.get(id=pk)
    if request.method == "POST":
        review.title = request.POST["title"]
        review.release_year=request.POST["release_year"]
        review.genre=request.POST["genre"]
        review.rating=request.POST["rating"]
        review.running_time=request.POST["running_time"]
        review.review=request.POST["review"]
        review.director=request.POST["director"]
        review.actors=request.POST["actors"]

        review.save()

        return redirect(f"/reviews/{pk}")
    context = {
        "review": review
    }
    return render(request, 'review_update.html', context)

def review_delete(request, pk):
    if request.method == "POST": 
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/reviews")