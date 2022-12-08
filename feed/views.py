from django.shortcuts import render,redirect
from feed.models import Tag,Post,Stream,Follow
from django.contrib.auth.decorators import login_required
from feed.forms import NewPostForm

# Create your views here.

############ HOME ############

def home(request):
    user = request.user
    posts = Stream.objects.filter(user=user)
    group_ids = []
    for post in posts:
        group_ids.append(post.post_id)
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    form = NewPostForm()
    newpost(request)
    context = {
        'post_items' : post_items,
        'form' : form,
    }

    return render(request,'home.html',context)

############ ADD NEW POST ############

def newpost(request):
    user = request.user.id
    tags_obj = []

    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tag')
            tags_list = list(tag_form.split(','))

            for tag in tags_list:
                t,created = Tag.objects.get_or_create(title=tag)
                tags_obj.append(t)

            p,created = Post.objects.get_or_create(picture=picture,caption=caption,user_id=user)
            p.tag.set(tags_obj)
            p.save()
            return redirect('/')
    else:
        form = NewPostForm()
    context = {
        'form' : form
    }
    return render(request,'newpost.html',context)

############ PROFILE ############

def profile(request):
    form = NewPostForm()
    newpost(request)
    context = {
        'form':form
    }
    return render(request,'profile.html',context)

############ CHAT ############

def chat(request):
    form = NewPostForm()
    newpost(request)
    context = {
        'form':form
    }
    return render(request,'chat.html',context)