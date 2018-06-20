from django.db import models

#다른엡에 선언된 모델과 관계 가지기위해 import함
from members.models import User


class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete= models.CASCADE,
        blank=True,
        null=True,
    )

    title = models.CharField(max_length=150)

    content = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

