from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import JsonResponse
from .forms import PostForm
from profiles.models import Profile
# def post_list_and_create(request):
#         form = PostForm(request.POST or None)
#         qs = Post.objects.all()

#         if request.is_ajax():
#               if form.is_valid():
#                     author = Profile.objects.get(user=request.user)
#                     instance = form.save(commit=False)
#                     instance.author = author
#                     instance.save()
#         return render(request, 'posts/main.html',{'qs':qs})

def post_list_and_create(request):
    form = PostForm(request.POST or None)
    #qs = Post.objects.all()

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if form.is_valid():
            author = Profile.objects.get(user=request.user)
            instance = form.save(commit=False)
            instance.author = author
            instance.save()        
            return JsonResponse({
                 'title': instance.title,
                 'body': instance.body,
                 'author': instance.author.user.username,
                 'id': instance.id,
            })
        # If form is invalid, return error response
       

    # For non-AJAX requests, render the HTML template
    context = {
         'form': form,
    }

    return render(request, 'posts/main.html', context)

def post_detail(request, pk):
    obj = Post.objects.get(pk=pk)
    form = PostForm()
    context = {
         'obj': obj,
         'form': form,
    } 
    return render(request, 'posts/detail.html', context)

def load_post_data_view(request, num_posts):
    visible = 3
    upper = num_posts
    lower = upper - visible
    size = Post.objects.all().count()

    qs = Post.objects.all()
    data = []
    for obj in qs:
            item = {
                    'id': obj.id,
                    'title': obj.title,
                    'body': obj.body,
                    'liked': True if request.user in obj.liked.all() else False,
                    'count': obj.like_count,
                    'author': obj.author.user.username
            }
            data.append(item)
    return JsonResponse({'data':data[lower:upper], 'size': size})

def post_detail_data_view(request, pk):
    obj = Post.objects.get(pk=pk)
    data = {
          'id': obj.id,
          'title': obj.title,
          'body': obj.body,
          'author':obj.author.user.username,
          'logged_in': request.user.username
    }
    return JsonResponse({'data': data})

# def like_unlike_post(request):
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         pk = request.POST.get('pk')
#         obj = Post.objects.get(pk=pk)
#         if request.user in obj.liked.all():
#             liked = False
#             obj.liked.remove(request.user)
#         else:
#             liked = True
#             obj.liked.add(request.user)
#         return JsonResponse({'liked': liked, 'count': obj.like_count})

def like_unlike_post(request, pk):
    if request.method == 'POST':
        #pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked': liked, 'count': obj.like_count})

def update_post(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_body = request.POST.get('body')
        obj.title = new_title
        obj.body = new_body
        obj.save()
    return JsonResponse({
        'title': new_title,
        'body': new_body,
    })

def delete_post(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.method == 'POST':
        obj.delete()
    return JsonResponse({})