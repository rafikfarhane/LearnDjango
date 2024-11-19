from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') #gets all the post-objeacts
    return render(request, 'posts/posts_list.html', {'posts': posts}) #Ort des templates, es weiß wo der allg. Template Ordner ist, wegen settings.py
#1.bring post-model
#2.get all the posts
#3 pass the data on the template, so we can use it in our post-list template
# third param. in render()
#für 'posts' wird das query-set posts gespeichert

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})