from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from blog.models import Blogpost
from blog.views import get_blog_queryset


# Create your views here:
blog_post_per_page = 10
def home_screen(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET.get('q','')
        context['query'] = str(query)
    blog_posts = sorted(get_blog_queryset(query),key=attrgetter('date_update'), reverse=True)
    

    #Pagination
    page = request.GET.get('page',1)
    blog_posts_paginator = Paginator(blog_posts, blog_post_per_page)    

    try:
        blog_posts = blog_posts_paginator.page(page) 
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator(blog_post_per_page)
    except EmptyPage:
        blog_posts = blog_posts_paginator(blog_post_paginator.num_pages)
    
    context['blog_posts'] = blog_posts

    return render(request, "personal/home.html",context)