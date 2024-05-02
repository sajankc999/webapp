from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(user,on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    caption = models.CharField(max_length = 150,null =True,blank =True)
    photo = models.ImageField(upload_to='user/images/',null=True,blank=True)
    like_count = models.PositiveIntegerField(default = 0)
    comment_count = models.PositiveIntegerField(default = 0)

class Interaction(models.Model):
    user = models.ForeignKey(user,on_delete= models.CASCADE)
    post = models.ForeignKey(Post,on_delete= models.CASCADE)
    has_liked = models.BooleanField(default =False,null=False)
    has_commented = models.BooleanField(default =False,null=False)
    comment = models.CharField(max_length = 200,null=True,blank=True)

    

    
