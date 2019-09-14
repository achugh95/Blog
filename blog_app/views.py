from django.shortcuts import render
from . models import *
from django.views.generic import ListView, DetailView
from . forms import PostForm                          # ModelForm to Create and Edit Post Objects
from django.utils import timezone

# Create your views here.


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = 'List_Posts.html'
    ordering = ['-created_date']


class PostDetail(DetailView):
    model = Post
    template_name = 'Detail_Post.html'


def create_post(request):
    print('Create Posts view has been called.')

    if request.method == "POST":
        form = PostForm(request.POST)
        print("POST")

        if form.is_valid():
            print("Valid")
            post = form.save(commit=False)
            post.created_date = timezone.now()
            # print(post.__dict__)
            post.save()

        return render(request, 'Post_Success.html')

    else:
        form = PostForm()

    return render(request, 'Create_Edit_Post.html', {'form': form})


def edit_post(request, pk):
    print('Edit Posts view has been called.')

    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        print("Post")
        print("Before:", post.created_date)
        post.created_date = timezone.now()
        form = PostForm(request.POST, instance=post)
        print("After:", post.created_date)
        print(form)

        if form.is_valid():
            print("Valid")
            form.save()
        return render(request, 'Post_Success.html')

    else:
        form = PostForm(instance=post)

    return render(request, 'Create_Edit_Post.html', {'form': form})


def contact_us(request):
    print('Contact Us view has been called.')

    return render(request, 'Contact_Us.html')
