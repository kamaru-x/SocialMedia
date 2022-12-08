from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    location = models.CharField(max_length=50,null=True,blank=True)
    url = models.URLField(max_length=2000,null=True,blank=True)
    bio = models.TextField(max_length=150,null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=user_directory_path,blank=True,null=True,verbose_name='picture')

    def __str__(self):
        return self.first_name