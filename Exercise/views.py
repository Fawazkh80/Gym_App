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
from datetime import date
from Account.serializers import UserSerializer

#--------------------------------------------INPUTS----------------------------------------------
@api_view(['POST'])
def CreateWeights(request):
    # latestWeight = User.objects.get(username=request.user).weight.all().order_by('created_at').first()
    # latestSerializer = serializers.WeightSerializer(latestWeight, many=False)
    volume = request.data['weight'] * request.data['reps'] * request.data['sets']
 

    serializer = serializers.WeightSerializer(data={    
    'exe_user':request.user.id,
    'exe_name' : request.data['exe_name'],
    'reps' : request.data['reps'],
    'rpe' : request.data['rpe'],
    'sets' : request.data['sets'],
    'weight' : request.data['weight'],
    'volume' : volume,
    'category':request.data['category'],
    'note':request.data['note']
    })


    if serializer.is_valid():
        serializer.save()

    data={
        'data':serializer.data,
        # 'latest':latestSerializer.data
    }
    return Response(data)




@api_view(['POST'])
def CreateCalories(request):
    # latestWeight = User.objects.get(username=request.user).inputs.all()
    Bmr = 13.397*request.data['user_weight'] + 4.799*request.data['height'] - 5.677*request.data['age'] + 88.362
    Calories = Bmr * request.data['activity']
    Protien = request.data['user_weight'] * 2
    Carb = (Calories * 0.5) / 4 
    Fat =  (Calories * 0.3) / 9 

    serializer = serializers.InputWeightSerializer(data={
        'input_user': request.user.id,     
        'user_weight': request.data['user_weight'],
        'height':request.data['height'],
        'age':request.data['age'],
        'calories':int(Calories),
        'protien':int(Protien),
        "carb":int(Carb),
        "fat":int(Fat),
        "percentage":0
    })
    
    
    if serializer.is_valid():
        serializer.save()
        print("saved")
    else:
      print(serializer.errors)

    data={
        'data':serializer.data,
    }
    return Response(data)
#--------------------------------------------PERCENTAGE----------------------------------------------
@api_view(['GET'])
def ProgressOverLoad(request):

    BestWeightObject = User.objects.get(username=request.user).weight.all().order_by("-created_at")
    BestWeightsWeight = BestWeightObject.order_by("-weight").first().weight
    BestWeightsVolume = BestWeightObject.order_by("-weight").first().volume

    DayExe = User.objects.get(username=request.user).weight.all().order_by('-created_at')
    AllDayExe = User.objects.get(username=request.user).weight.filter(created_at=DayExe.first().created_at)
    volumeSum = 0
    if AllDayExe.count() > 1:
        for key in AllDayExe:
            volumeSum = volumeSum + key.volume
    elif AllDayExe.count() == 1:
        for key in AllDayExe:
            volumeSum = key.volume

    lastDayExe = User.objects.get(username=request.user).weight.filter(category=DayExe.first().category).order_by('-created_at')

    previousDay = 0

    for key in lastDayExe:
        if(key.created_at < DayExe.first().created_at):
            exeDate = key.created_at
            beforeLastExe=User.objects.get(username=request.user).weight.filter(created_at=exeDate).first()
            previousDay = beforeLastExe.created_at
            break


    before_DayExe =  User.objects.get(username=request.user).weight.filter(created_at=previousDay)
    previousDayVolumeSum = 0
    if before_DayExe.count() > 1:
        for key in before_DayExe:
            previousDayVolumeSum = previousDayVolumeSum + key.volume
    elif before_DayExe.count() == 1:
        for key in before_DayExe:
            previousDayVolumeSum = key.volume


    data={
        'volume_sum_last':volumeSum,
        'volume_sum_before_last':previousDayVolumeSum,
        'best_weight_weight':BestWeightsWeight,
        'best_weight_volume':BestWeightsVolume,
        'percentage':(volumeSum * 100)/previousDayVolumeSum,
    }
    return Response(data)

#PERCENTAGE REQUEST.DATA['FIELDS'] NSBT ALT6AB8 Error
@api_view(['PUT'])
def CalPercentage(request):
    lastInput = User.objects.get(username=request.user).inputs.all().order_by("-created_at").first()
    lastCalories = lastInput.calories 
    DayCalories = request.data['calories_ate']
    percentage = (DayCalories * 100) / lastCalories
    serializer = serializers.InputWeightSerializer(instance=lastInput ,data={
    'percentage' : int(percentage)
    })
    lastInputSerializer = serializers.InputWeightSerializer(lastInput, many=False)

    if serializer.is_valid():
      serializer.save()

    data ={
    'data' : serializer.data,
    'calories_data' : lastInputSerializer.data,
    }
    return Response(data)

#--------------------------------------------HISTORY----------------------------------------------




#--------------------------------------------LEADERBOARD(ALL USERS)----------------------------------------------
#ALL USERS ORDERED BY VOLUME
@api_view(['GET'])
def leaderBoard(request):
    allUsers = User.objects.all()

    allVolumesOrdered = []
    allUsersOrdered = []
    temp = 0

    for dict in allUsers:
        allVolumesOrdered.append(dict.weight.all().order_by('-volume').first())

    for i in range(0,len(allVolumesOrdered)):
        for j in range(i+1,len(allVolumesOrdered)):
          if(allVolumesOrdered[i].volume<allVolumesOrdered[j].volume):
            temp = allVolumesOrdered[i].volume
            allVolumesOrdered[i].volume = allVolumesOrdered[j].volume
            allVolumesOrdered[j].volume = temp

    for dict in allVolumesOrdered:
      allUsersOrdered.append(dict.exe_user)

    serializer2 = serializers.WeightSerializer(allVolumesOrdered, many = True)
    serializer1 = UserSerializer(allUsersOrdered, many = True)

    data={
    'Data': {
      'weight_data':serializer2.data,
      'user_data':serializer1.data, #I JUST HOPE IT WOKRED 
    }
    }

    return Response(data)
#--------------------------------------------GET ONE (DETAIL) FOR WEIGHTS AND CALROIES----------------------------------------------


#WEIGHTS-> ALL WEIGHT FIELDS Done
@api_view(['GET'])
def OneWeights(request,id):
  oneWeight = models.weights.objects.get(id=id)
  serializer = serializers.WeightSerializer(oneWeight, many = False)

  data={
    'Data': serializer.data
  }

  return Response(data)

#CALORIESS-> ALL CALORIES FIELDS Done
@api_view(['GET'])
def OneCalories(request,id):
  oneCalories=models.inputweights.objects.get(id=id)
  serializer = serializers.InputWeightSerializer(oneCalories, many = False)

  data={
    'Data': serializer.data
  }

  return Response(data)
#--------------------------------------------Get all Caloreis detials by id{Response Error} ------------------------------------------
@api_view(['GET'])
def CaloriesIndex(request):
  AllCalories=User.objects.get(username = request.user).inputs.all()
  serializer = serializers.InputWeightSerializer(AllCalories, many = True)

  data={
    'Data': serializer.data
  }

  return Response(data)
#--------------------------------------------Get all Weights detials by id{Response Error} ------------------------------------------
@api_view(['GET'])
def WeightsIndex(request):
  # oneWeight = models.weights.objects.filter(exe_user=request.user.id).order_by("-created_at")
  AllWeights = User.objects.get(username=request.user).weight.all()
  
  serializer = serializers.WeightSerializer(AllWeights, many = True)


  data={
    'Data': serializer.data
  }

  return Response(data)


#--------------------------------------------DELETE (WEIGHTS AND CALORIES) Done ------------------------------------------

@api_view(['DELETE'])
def DeleteWeights(request,id):
  OneWeight = models.weights.objects.get(id=id)
  OneWeight.delete()
  data = {
    'succses' : 'weights information was deleted'
  }
  return Response(data)


@api_view(['DELETE'])
def DeleteCalories(request,id):
  OneCaalore = models.inputweights.objects.get(id=id)
  OneCaalore.delete()
  data = {
    'succses' : 'weights information was deleted'
  }
  return Response(data)







