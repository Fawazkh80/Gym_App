from django.db import models
from django.contrib.auth.models import User



class weights(models.Model):
    exe_name = models.TextField(max_length = 100, blank=True)
    note = models.TextField(max_length = 500, blank=True)
    category = models.CharField(max_length = 100, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    sets = models.IntegerField(null=True, blank=True)
    rpe = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True,)
    exe_user = models.ForeignKey(User, related_name="weight", on_delete=models.CASCADE) 

class inputweights(models.Model):
    user_weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    protien = models.IntegerField(null=True, blank=True)
    carb = models.IntegerField(null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)
    fat= models.IntegerField(null=True, blank=True)
    percentage= models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True,)
    input_user = models.ForeignKey(User, related_name="inputs", on_delete=models.CASCADE) 