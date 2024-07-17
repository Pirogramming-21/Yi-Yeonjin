from django.db import models
from apps.develTools.models import DevelTool

# Create your models here.
class Post(models.Model):
  title = models.CharField('아이디어명', max_length=24)
  image = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
  content = models.CharField('내용', max_length=24)
  interest = models.IntegerField('아이디어 관심도')
  # 작성자
  devtool = models.ForeignKey(DevelTool, on_delete=models.CASCADE, verbose_name='예상 개발툴', null=True)

class IdeaStar(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)