from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        exclude = ("author_id",)
        labels = {
            "title": "Title:",
            "Body": "Content:"
        }
