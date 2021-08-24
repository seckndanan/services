from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.acceuil_list,name='Acceuil'),
]

