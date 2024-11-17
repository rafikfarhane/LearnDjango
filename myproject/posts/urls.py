from django.urls import path
from .import views

urlpatterns = [
    path('', views.posts_list), # we are already in the posts path so -> ''
    #it knows to look in our new templates directory in posts, for the posts_lists template 
]