from django.shortcuts import render
from blog.models import Post
from blog.models import Comment
from .forms import CommentForm
from django.http import HttpResponseBadRequest

# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__iexact=category
    ).order_by('-created_on')

    context = {
        "category": category,
        "posts": posts
    }

    if len(posts.values()) == 0:
        return HttpResponseBadRequest()
    else:
        return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)
