from django.shortcuts import render,redirect

# Create your views here.
from .models import contact
from django.forms import fields

def contact_list(request):
    contact_list=contact.objects.all
    template = 'contact/contact.html'
    context = {
        'contact_list': contact_list,
    }
    if request.method=='POST':
       new_contact = contact(
           nom = request.POST['nom'],
           prenom =request.POST['prenom'],
           message =request.POST['message'],
           email =request.POST['email'],
           telephone =request.POST['telephone']
       )
       new_contact.save()
       return redirect('Contact')

    return render(request, template, context)

