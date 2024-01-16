from django.shortcuts import render
from .models import Post, Category, Author
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):

    queryset = request.GET.get("search")
    posts = Post.objects.filter(state = True)

    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset),
            state = True,
        ).distinct()
    
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts':posts})

def tutorials (request):
    queryset = request.GET.get("search")
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact='Tutorial')
        )
    
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset),
            state = True,
            category = Category.objects.get(name__iexact = 'Tutorial'),
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'tutorials.html', {'posts':posts})

def techtrends (request):
    queryset = request.GET.get("search")
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact='Technology')
        )
    
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset),
            state = True,
            category = Category.objects.get(name__iexact = 'Technology'),
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'techtrends.html', {'posts':posts})

def videogames (request):
    queryset = request.GET.get("search")
    posts = Post.objects.filter(
        state = True,
        category = Category.objects.get(name__iexact='Videogames')
        )
    
    if queryset:
        posts = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(description__icontains = queryset),
            state = True,
            category = Category.objects.get(name__iexact = 'Videogames'),
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'videogames.html', {'posts':posts})

def postDetail(request, slug):
    # post = Post.objects.get(slug=slug)
    # print(post.image)
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'postDetail':post})
