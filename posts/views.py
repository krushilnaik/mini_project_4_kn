from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm
from .models import Post


# Create your views here.
def index(request):
    """
    Return all posts
    """

    return Post.objects.all()


def create(request):
    """
    /create
    """

    if request.method == "POST":
        form = PostForm(request.POST)
        form.author = request.user

        if form.is_valid():
            form.save()
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
