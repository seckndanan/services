from django.shortcuts import render

# Create your views here.
from .models import acceuil

def acceuil_list(request):
    acceuil_list=acceuil.objects.all
    template = 'acceuil/acceuil.html'
    context = {
        'acceuil_list': acceuil_list
    }
    return render(request, template, context)
