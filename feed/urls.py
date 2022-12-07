from feed import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('chat/',views.chat,name='chat')
]