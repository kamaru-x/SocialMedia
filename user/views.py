from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from user.models import Profile
from feed.models import Post,Follow
from django.urls import resolve
from django.core.paginator import Paginator

# Create your views here.

############ user profile ############

def userrofile(request,username):
    user = get_object_or_404(User,username=username)
    profile = Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name
    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')
    else:
        pass

    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    post_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    context = {
        'posts_paginator' : posts_paginator,
        'profile' : profile,
        'posts' : posts,
        'post_count' : post_count,
        'following_count' : following_count,
        'followers_count' : followers_count,
    }

    return render(request, 'profile.html',context)