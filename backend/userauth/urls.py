from .views import *
from django.urls import path

urlpatterns = [
    path('signin',signin),
    path('login',login),
    path('register',register)
    # path('signout',signout),
   
]
