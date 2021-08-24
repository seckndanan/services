from django.shortcuts import render,HttpResponse
from .models import partenaire

# Create your views here.
def partenaire_list(request):
    partenaire_list = partenaire.objects.all
    template = 'partenaire/list.html'
    context = {
        'partenaire_list': partenaire_list
    }
    return render(request, template, context)