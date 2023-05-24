from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import PostForm
from .models import Post
from .serializers import PostSerializer


@api_view(['GET'])
def posts(request):
    """
    /all
    """

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

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


def edit(request, post_id):
    """
    /edit/:post_id
    """
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        form = PostForm(instance=post, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = PostForm(instance=post)

    return render(request, 'edit.html', {'post': post, 'form': form})


def delete(request, post_id):
    """
    /delete/:post_id
    """

    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('home')
