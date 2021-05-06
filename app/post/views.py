from django.shortcuts import render, redirect
from post.models import Post
from post.form import PostForm
# Create your views here.
def post(request):
    data = Post.objects.all()
    context = {
        'data': data
    }
    return render(request, 'postTemplate.html', context)

def createPost(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    return render(request, 'formPost.html', {'form': form})

def updatePost(request, id):
    post = Post.objects.get(id = id)
    if request.method == 'GET':
        form = PostForm(instance= post)
    else:
        form = PostForm(request.POST, instance= post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    return render(request, 'formPost.html', {'form': form})

def deletePost(request, id):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('post_list')
