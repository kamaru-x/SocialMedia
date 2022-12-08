from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from user.models import Profile
from feed.models import Post,Follow,Stream
from django.urls import resolve
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from user.forms import EditProfileForm

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

    follow_status = Follow.objects.filter(following=user,follower=request.user).exists()

    context = {
        'posts_paginator' : posts_paginator,
        'profile' : profile,
        'posts' : posts,
        'post_count' : post_count,
        'following_count' : following_count,
        'followers_count' : followers_count,
        'follow_status' : follow_status,
    }

    return render(request, 'profile.html',context)

############ edit user profile ############

def editprofile(request):
    user = request.user
    profile = Profile.objects.get(user__id=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile.image = form.changed_data.get('picture')
            profile.first_name = form.changed_data.get('first_name')
            profile.last_name = form.changed_data.get('last_name')
            profile.location = form.changed_data.get('location')
            profile.url = form.changed_data.get('url')
            profile.bio = form.changed_data.get('bio')
            profile.created = form.changed_data.get('created')
            profile.save()
            return redirect('profile')
    else:
        form = EditProfileForm()

    context = {
        'form' : form
    }

    return render(request,'profile.html',context)



############ user profile ############

def follow(request,username,option):
    user = request.user
    following = get_object_or_404(User,username=username)
    try:
        f,created = Follow.objects.get_or_create(follower=user,following=following)
        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following,user=user).all().delete()
        else:
            posts = Post.objects.filter(user=following)[:10]

            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post,user=user,date=post.posted,following=following)
                    stream.save()

        return HttpResponseRedirect(reverse('profile',args=[username]))
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse('profile',args=[username]))