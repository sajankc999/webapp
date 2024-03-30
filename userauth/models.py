from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100,null=True,blank=True)
    last_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 10,null=True,blank=True)
    email = models.EmailField(max_length = 100,unique = True)
    # username = models.CharField(max_length=150)
    female = "F"
    male ="M"
    others ='O'
    Gender =(
        (female,"female"),
        (male,"Male"),
        (others,"others")
    )
    gender = models.CharField(max_length=50, choices = Gender,default = male)
    DOB = models.DateField()
    profile_picture = models.ImageField(upload_to='user_pfps/',null= True,blank=True)



    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS=[]

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_normal_user = models.BooleanField(default = True)
    
    date_joined = models.DateTimeField(default = timezone.now)
