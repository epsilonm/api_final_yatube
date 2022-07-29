from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(Group,
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL
                              )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(User,
                             related_name='follower',
                             verbose_name='Follower',
                             on_delete=models.CASCADE)
    following = models.ForeignKey(User,
                                  related_name='following',
                                  verbose_name='Author',
                                  on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['following', 'user'],
                name='unique_following'
            ),
            models.CheckConstraint(check=~models.Q(user=models.F('following')),
                                   name='check_following')
        ]

    def __str__(self):
        return f'User {self.user} has followed on {self.following}'
