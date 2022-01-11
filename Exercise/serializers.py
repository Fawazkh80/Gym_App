from rest_framework import serializers
from . import models
class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.weights
        fields =  '__all__'
        
class InputWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.inputweights
        fields =  '__all__'