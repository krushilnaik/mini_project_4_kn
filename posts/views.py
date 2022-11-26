from django.shortcuts import render

from models import Post


# Create your views here.
def index():
    """
    Return all posts
    """

    return Post.objects.all()


def create():
    """
    /create
    """

    return "TBA"


def edit():
    """
    /edit/:post_id
    """

    return "TBA"


def delete():
    """
    /delete/:post_id
    """

    return "TBA"
