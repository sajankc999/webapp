from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import generics,ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import *
from rest_framework.response import Response


# Create your views here.

class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes =[IsAuthor,]

    # def get_queryset(self):
    #     return Post.objects.filter(author=self.request.user)
    def update(self, request, *args, **kwargs):
        return Response('post cant be edited')

class InteractionView(ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [IsOwner,]

    def update(self, request, *args, **kwargs):
        return Response({'message':'interactions cannot be updated'})