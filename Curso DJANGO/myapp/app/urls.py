from django.urls import path
from app import views as app
from . import views

     

urlpatterns = [
    path('', views.index)
   
]
