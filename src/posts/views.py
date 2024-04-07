from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import JsonResponse

def post_list_and_create(request):
        qs = Post.objects.all()
        return render(request, 'posts/main.html',{'qs':qs})

def hello_world_view(request):
            return JsonResponse({'text': 'hello world'})