from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField('제목', max_length=100)
    image = models.ImageField('이미지', upload_to='posts/%Y%m%d')
    content = models.TextField('내용')
    like = models.IntegerField('좋아요',default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)