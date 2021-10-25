from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {'posts': posts, }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Yatube'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)
