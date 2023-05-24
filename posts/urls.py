from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("all", views.posts, name="posts"),
    path("create", views.create, name="create"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("delete/<int:post_id>", views.delete, name="delete")
]
