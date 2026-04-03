from django.shortcuts import render
from django.shortcuts import HttpResponse
from monapp.models import Utilisateur,Programme,Programmeechauffement,Activité

def accueil(request) :
    utilisateurs=Utilisateur.objects.all()
    return render(request,'monapp/accueil.html',{'utilisateurs': utilisateurs})



def liste_programmes(request):
    programmes=Programme.objects.all()
    
    return render(request, 'monapp/liste_programmes.html', {'programmes':programmes})

def programme_détails(request,id) :
    programme=Programme.objects.get(id=id) #pour donner les détails d'un programme en particulier

    return render(request, 'monapp/programme_détails.html', {'programme': programme})


    

# Create your views here.
