from django.urls import path
from user import views

urlpatterns = [
    path('<username>/',views.userrofile,name='profile'),
    path('<username>/follow/<option>',views.follow,name='follow')
]