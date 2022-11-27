# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Post model"""

    created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=64)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
