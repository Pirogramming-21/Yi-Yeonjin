from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100) #제목
    release_year = models.IntegerField()  # 개봉년도
    genre = models.CharField(max_length=20)  # 장르
    rating = models.FloatField()  # 별점
    running_time = models.IntegerField()  # 러닝타임
    review = models.TextField()  # 리뷰
    director = models.CharField(max_length=100)  # 감독
    actors = models.TextField()  # 배우 (여러 명일 경우 콤마로 구분)