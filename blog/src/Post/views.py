# This file for getting information form DB.
from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Create your views here.
from .models import Post
from .forms import PostForm


def all_post(request):
    all_posts = Post.objects.all()
    context = {
         'all_posts': all_posts,
    }
    return render(request, 'all_posts.html',context)

def post(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post,id=id)
    context = {
        'post': post,
    }

    return render(request,'detail.html',context)

def create_post(request):
    # Check if method for Form is POST or GET
    # If it is POST this is mean the data is encrypt
    # else that mean the data is not encrypt.
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request,'create.html',context)