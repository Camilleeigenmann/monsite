from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from monapp.models import Utilisateur,Programme,Programmeechauffement,Activité
from monapp.forms import Ajouter_activité_form

def accueil(request) :
    utilisateurs=Utilisateur.objects.all()
    return render(request,'monapp/accueil.html',{'utilisateurs': utilisateurs})





def liste_programmes(request):
    programmes=Programme.objects.all()
    
    return render(request, 'monapp/liste_programmes.html', {'programmes':programmes})

def programme_détails(request,id) :
    programme=Programme.objects.get(id=id) #pour donner les détails d'un programme en particulier

    return render(request, 'monapp/programme_détails.html', {'programme': programme})







def liste_activités(request,id) :
    utilisateur=Utilisateur.objects.get(id=id)
    activités=Activité.objects.filter(utilisateur=id)
    
# les activités liés à cet utilisateur seront donc séléctionnées puis affichées (un seul dictionnaire sinon ça bug)
    return render(request, 'monapp/liste_activités.html', {'activités':activités , 'utilisateur': utilisateur})

def activité_détails(request,id):
    activité=Activité.objects.get(id=id)
    programme=activité.programme
    utilisateur=activité.utilisateur

    return render(request,'monapp/activité_détails.html', {'activité':activité, 'programme':programme , 'utilisateur':utilisateur})

def ajouter_activité(request,id) :
    utilisateur_utilisé=Utilisateur.objects.get(id=id)
    if request.method =='POST' :
        form =Ajouter_activité_form(request.POST)
        if form.is_valid() :
            activité= form.save(commit=False)   # arrêter la création de l'objet pour remplir le champ utilisateur avec l'id donnée
            activité.utilisateur= utilisateur_utilisé    #lier mannuellement l'activité à un utilisateur(pas son id)
            activité.save()    # créer une nouvelle activité et la stocker dans la db
            return redirect('activité-détails',activité.id)    # redirige vers la liste d'activités de l'utilisateur
    else :
        form= Ajouter_activité_form() # méthode GET

    return render(request, 'monapp/ajouter_activité.html', {'form': form})

def modifier_activité(request,id) :
    activité = Activité.objects.get(id=id)
    if request.method =='POST' :
        form =Ajouter_activité_form(request.POST,instance=activité) # on pré-rempli un formulaire avec une activité déjà existant
        if form.is_valid :
            # mettre à jour l'activité déjà existante
            form.save() 
            # rediriger vers les détails de l'activité
            return redirect('activité-details', activité.id)
    else :
        form = Ajouter_activité_form(instance=activité)

    return render(request, 'monapp/modifier_activité.html', {'form': form, 'activité':activité})

def supprimer_activité(request,id) :
    activité= Activité.objects.get(id=id)
    utilisateur=activité.utilisateur
    if request.method == 'POST' :
        # supprimer le groupe de la base de donnée
        activité.delete()
        return redirect( 'liste-activités', utilisateur.id)
    return render(request, 'monapp/supprimer_activité.html', {'activité': activité})

    

# Create your views here.
