from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Blogpost
from django.db.models import Q
from django.http import HttpResponse
from blog.forms import Createblogpost,Updateblogpostform
from account.models import Account


def create_blog_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect ('must_authenticate')
    
    form = Createblogpost(request.POST or None , request.FILES or None)     
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.object.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form=  Createblogpost()
        context['success_message'] = "Posted"
    else:
        context['error_message'] = "Failed to post."
    
    context['form'] = form
    return render(request, 'blog/create_blog.html',context)

def detail_blog_view(request,slug):
    context = {}
    blog_post = get_object_or_404(Blogpost,slug=slug)
    context['blog_post'] = blog_post
    return render(request, 'blog/detail_blog.html',context)

def edit_blog_view(request,slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    
    blog_post = get_object_or_404(Blogpost,slug=slug)

    if blog_post.author != user:
        return HttpResponse("You are not the author of the post ! ")
        
    if request.POST:
        form = Updateblogpostform(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj=form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
    form = Updateblogpostform(
        initial={
            "title":blog_post.title,
            "body":blog_post.body,
            "image":blog_post.image,
        }
    )
    context['form'] = form
    return render(request,"blog/edit_blog.html",context)

def get_blog_queryset(query=None):
    queryset = []
    queries=query.split(" ") #This gonna split the words and put then into list individually. eg: About Money = ['About','Money']
    for q in queries:
        posts = Blogpost.objects.filter(
            Q(title__icontains=q)
            ).distinct()
        for post in posts:
            queryset.append(post)
    return list(set(queryset))

def delete_blog_view(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    blog_post = get_object_or_404(Blogpost, slug=slug)
    if blog_post.author != user:
        return HttpResponse("You are not the author of the post!")

    if request.method == 'POST':
        blog_post.delete()

    context = {}
    return render(request,"blog/delete_blog.html", context)



