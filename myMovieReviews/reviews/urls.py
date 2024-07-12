from django.urls import path
from .views import *

app_name = 'reviews'

urlpatterns = [
    path('',review_list),
    path('create/',review_create),
    path('<int:pk>/', review_detail),
]