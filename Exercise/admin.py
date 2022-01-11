from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.weights)
admin.site.register(models.inputweights)