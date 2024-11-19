from django.urls import path
from .import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"), # we are already in the posts path so -> ''
    path('<slug:slug>', views.post_page, name="page") # we are already in the posts path so -> ''
    #it knows to look in our new templates directory in posts, for the posts_lists template 
]