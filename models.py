"""
Django models of database schema
"""

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Post model"""

    created = models.DateTimeField()
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=1200)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
