from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
  path('', main, name='main'), 
  path('create/', create, name='create'),
  path('detail/<int:pk>/', detail, name='detail'),
  path('delete/<int:pk>/', delete, name='delete'),
  path('update/<int:pk>/', update, name='update'),
  path('update_interest/<int:pk>/<str:btn>/', update_interest, name='update_interest'),
  path('update_star/<int:pk>/<str:action>/', update_star, name='update_star'),
]