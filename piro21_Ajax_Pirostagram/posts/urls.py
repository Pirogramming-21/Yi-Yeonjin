from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.main, name='main'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('like/', views.like, name='like'),
    path('comment/<int:pk>/', views.comment, name='comment'),
    path('comment/delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]