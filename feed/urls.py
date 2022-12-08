from feed import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('tags/<slug:tag_slug>/',views.tags,name='tags'),
    # path('profile/',views.profile,name='profile'),
    path('chat/',views.chat,name='chat'),
    path('<uuid:post_id>/like',views.like,name='like')
]