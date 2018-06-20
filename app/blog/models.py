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

    def __str__(self):
        return f'title: {self.title}, content: {self.content}, user: {self.user.name}, date: {self.created_at}'

    @property
    def like_users(self):

        user_name_list = []

        for postlike in self.postlike_set.all():
            user_name_list.append(postlike.user.name)

        return User.objects.filter(name__in = user_name_list)


class PostLike(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # related_name= 'comments'
    )

    content = models.CharField(max_length=300, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'title: {self.post.title}, content: {self.content}, user: {self.user.name}, date: {self.created_at}'


    @property
    def like_users(self):

        user_name_list = []

        for commentlike in self.commentlike_set.all():
            user_name_list.append(commentlike.user.name)

        return User.objects.filter(name__in = user_name_list)


class CommentLike(models.Model):

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comment: {self.comment}'