from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Post


# Create your views here.
def index(request):
    """
    Return all posts
    """

    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})


def create(request):
    """
    /create
    """

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/posts')
    else:
        form = PostForm()

    return render(request, 'create.html', {'form': form})


def edit(request):
    """
    /edit/:post_id
    """

    return HttpResponse("TBA")


def delete(request):
    """
    /delete/:post_id
    """

    return HttpResponse("TBA")
