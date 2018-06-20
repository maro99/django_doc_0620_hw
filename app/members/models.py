from django.db import models



class User(models.Model):
    name = models.CharField(max_length=50)

    friends = models.ManyToManyField(
        'self',
    )

    block_users = models.ManyToManyField(
        'self',
        symmetrical=False,
    )

    def __str__(self):
        return f'name: {self.name}'

    # str에서 다같이 출력하려면 애러가 난다. 배운대로 property로 따로 friends, block리스트 보는것 추가함.
    @property
    def friends_list(self):
        return self.friends.all()

    @property
    def block_list(self):
        return self.block_users.all()



    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def posts(self):
        return self.post_set.all()


class UserInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    address = models.CharField(max_length=150)
    phone_number = models.IntegerField()

    def __str__(self):
        return f'user_name = {self.user.name}, address = {self.address}, ph : {self.phone_number}'

