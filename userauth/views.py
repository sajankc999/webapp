from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet,generics
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerailizer,UserLoginSerializer
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view 
# Create your views here.
user_obj = get_user_model()

@api_view(['POST'])
def register(request):
    serializer = UserRegisterSerailizer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    password = serializer.validated_data.get('password')
    first_name = serializer.validated_data.get('first_name')
    last_name = serializer.validated_data.get('last_name')
    middle_name = serializer.validated_data.get('middle_name')
    phone_number = serializer.validated_data.get('phone_number')
    gender = serializer.validated_data.get('gender')
    DOB = serializer.validated_data.get('DOB')
    
    user = user_obj.objects.create(email=email,
                                    password=password,
                                    first_name=first_name,
                                    last_name=last_name,
                                    middle_name=middle_name,
                                    phone_number=phone_number,
                                    gender=gender,
                                    DOB=DOB)

    if user:
       
        return Response('user has been created')
    return Response("something went wrong")
    

@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    user = authenticate(username = email,password=password)
    if user:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({
            "username":user.get_username(),
            "token":token.key,
        })
    return  Response(user)
