from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request, 'posts/posts_list.html') #Ort des templates, es weiß wo der allg. Template Ordner ist, wegen settings.py
