from . import models
from . import serializers

from rest_framework.decorators import (
  api_view,
  permission_classes
)
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage

@api_view(['POST'])
def Register(request):

    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      user = User.objects.get(username=serializer.data['username'], password=serializer.data['password'])
      token = Token.objects.create(user=user) 

    else:
      print(serializer.errors)
    tk = Token.objects.get(user=user).key
    data = {
      # 'user_id':serializer.data['id'],
      'username':serializer.data['username'],
      'Token':tk,
    }
    return Response(data)

@api_view(['POST'])
def Login(request):
    username = request.data["username"]
    password = request.data["password"]


    try:
        
        user = User.objects.get(username=username, password=password)
    except ObjectDoesNotExist:
        print("wrong 505")

    serializer = serializers.UserSerializer(user,many=False)
  
    data = {
      "user":serializer.data,
      "token": Token.objects.get(user=user).key
    }
    return Response(data)

@api_view(['POST'])
def Logout(request):
    if(request.user != None):
    
        request.user.auth_token.delete()
    else:
        print("no data found in database\n")

    
    data = {
      'status':'Success!'
    }
    return Response(data)
    