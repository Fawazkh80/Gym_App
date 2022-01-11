from . import views
from django.urls import path
urlpatterns = [
    path('CreateWeight/', views.CreateWeights), #DONE
    path('CreateCalories/', views.CreateCalories), #DONE

    path('ProgressOverLoad/', views.ProgressOverLoad), #DONE
    path('CalPercentage/', views.CalPercentage), #DONE

    path('OneWeight/<int:id>/', views.OneWeights), #DONE
    path('OneCalorie/<int:id>/', views.OneCalories), #DONE

    path('CaloriesIndex/', views.CaloriesIndex), #DONE
    path('WeightsIndex/', views.WeightsIndex), #DONE

    path('DeleteWeights/<int:id>/', views.DeleteWeights),# DONE
    path('DeleteCalories/<int:id>/', views.DeleteCalories),#DONE

    path('leaderBoard/', views.leaderBoard),
]