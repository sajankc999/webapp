from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
# Create your models here.hone_number


class CustomManager(UserManager):
    def _create_user(self, email:str,password,username=None , **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if username is None:
            username = email.split("@")[0]
        user = User(email=email,username = username,**extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, email,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email,username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)

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
    DOB = models.DateField(auto_now=True)
    profile_picture = models.ImageField(upload_to='user_pfps/',null= True,blank=True)



    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS=[]

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_normal_user = models.BooleanField(default = True)
    
    date_joined = models.DateTimeField(default = timezone.now)
    objects=CustomManager()
