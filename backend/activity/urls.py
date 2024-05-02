from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('posts',PostView,basename='feed')
router.register('interaction',InteractionView,basename='interaction')
urlpatterns = [
    
]+router.urls
