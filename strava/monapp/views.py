from django.shortcuts import render
from django.shortcuts import HttpResponse

def accueil(request) :
    return render(request,'monapp/accueil.html' )
    

# Create your views here.
