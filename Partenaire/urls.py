from django.urls import path
from.import views

urlpatterns = [

    path('',views.partenaire_list,name='Partenaire'),

]