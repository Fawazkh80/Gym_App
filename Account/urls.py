from . import views
from django.urls import path
urlpatterns = [

    path('Register/', views.Register),
    path('Login/', views.Login),
    path('Logout/', views.Logout),

]
