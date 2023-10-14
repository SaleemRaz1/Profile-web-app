from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(default="Saleem KHan(default)" ,max_length=100,null=True)
    title=models.CharField(default="this is default",max_length=200)
    desc_text='this is default text area'
    desc=models.TextField(default=desc_text,max_length=200,null=True)
    profile_image=models.ImageField(default='media/default.jpg',upload_to='media',null=True,blank=True)
    def __str__(self):
        return "{self.user.username}'s profile"
    
