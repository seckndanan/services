from django.shortcuts import render

# Create your views here.
from .models import apropos

def apropos_list(request):
    apropos_list=apropos.objects.all
    template = 'apropos/apropos.html'
    context = {
        'apropos_list': apropos_list
    }
    return render(request, template, context)

