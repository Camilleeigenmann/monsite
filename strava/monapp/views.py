from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from monapp.models import Utilisateur,Programme,Programmeechauffement,Activité
from monapp.forms import Ajouter_activité_form, Créer_programme_form,Ajouter_activitéprogramme_form
from django.utils import timezone
def accueil(request) :
    utilisateurs=Utilisateur.objects.all()
    return render(request,'monapp/accueil.html',{'utilisateurs': utilisateurs})



def accueil_utilisateur(request, id ):
    utilisateur=Utilisateur.objects.get(id=id)
    now=timezone.now()
    mois_actuel=now.month
    annee_actuelle=now.year

    activites_du_mois=Activité.objects.filter(utilisateur_id=utilisateur.id,date__year=now.year,date__month=now.month)
    nb_activites_technique_mois=0
    nb_activites_puissance_mois=0
    nb_activites_endurance_mois=0
    nb_activites_autre_mois=0
    nb_activites_grimpe_libre_mois=0
    for activite in activites_du_mois :
        if activite.but=='Technique' :
            nb_activites_technique_mois +=1
        if activite.but=='Puissance':
            nb_activites_puissance_mois +=1
        if activite.but=='Endurance' :
            nb_activites_endurance_mois +=1
        if activite.but=='Autre' :
            nb_activites_autre_mois +=1
        if activite.but=='Grimpe libre' :
            nb_activites_grimpe_libre_mois +=1
    

    activites_annee=Activité.objects.filter(utilisateur_id=utilisateur.id,date__year=now.year)
    nb_activites_technique_annee=0
    nb_activites_puissance_annee=0
    nb_activites_endurance_annee=0
    nb_activites_autre_annee=0
    nb_activites_grimpe_libre_annee=0
    for activite in activites_annee :
        if activite.but=='Technique' :
            nb_activites_technique_annee +=1
        if activite.but=='Puissance':
            nb_activites_puissance_annee +=1
        if activite.but=='Endurance' :
            nb_activites_endurance_annee +=1
        if activite.but=='Autre' :
            nb_activites_autre_annee +=1
        if activite.but=='Grimpe libre' :
            nb_activites_grimpe_libre_annee +=1

    return render(request,'monapp/accueil_utilisateur.html', {'utilisateur':utilisateur,'mois_actuel':mois_actuel,
    'annee_actuelle':annee_actuelle,'activites_du_mois':activites_du_mois,'activites_annee':activites_annee
    ,'nb_activites_technique_mois':nb_activites_technique_mois, 'nb_activites_puissance_mois':nb_activites_puissance_mois
    ,'nb_activites_endurance_mois':nb_activites_endurance_mois,'nb_activites_autre_mois':nb_activites_autre_mois
    ,'nb_activites_grimpe_libre_mois':nb_activites_grimpe_libre_mois
    ,'nb_activites_technique_annee':nb_activites_technique_annee,'nb_activites_puissance_annee':nb_activites_puissance_annee
    ,'nb_activites_endurance_annee':nb_activites_autre_mois,'nb_activites_autre_annee':nb_activites_autre_annee
    ,'nb_activites_grimpe_libre_annee':nb_activites_grimpe_libre_annee})

def liste_programmes(request,id):
    utilisateur=Utilisateur.objects.get(id=id)

    programmes=Programme.objects.all()
    programmes_technique=Programme.objects.filter(but='Technique',utilisateur__isnull=True)
    programmes_puissance=Programme.objects.filter(but='Puissance',utilisateur__isnull=True)
    programmes_endurance=Programme.objects.filter(but='Endurance',utilisateur__isnull=True)
    programmes_autre=Programme.objects.filter(but='Autre',utilisateur__isnull=True)
    
    programmescréés=Programme.objects.filter(utilisateur=id)
    programmescréés_technique=Programme.objects.filter(but='Technique',utilisateur_id=utilisateur.id)
    programmescréés_puissance=Programme.objects.filter(but='Puissance',utilisateur_id=utilisateur.id)
    programmescréés_endurance=Programme.objects.filter(but='Endurance',utilisateur_id=utilisateur.id)
    programmescréés_autre=Programme.objects.filter(but='Autre',utilisateur_id=utilisateur.id)
    # pour classer les programmes en fonction de leurs but dans la page "liste_programmes"
    
    return render(request, 'monapp/liste_programmes.html', {'programmes':programmes, 'utilisateur':utilisateur,'programmescréés':programmescréés,
    'programmes_technique':programmes_technique,'programmes_puissance':programmes_puissance,'programmes_endurance':programmes_endurance,'programmes_autre':programmes_autre,
    'programmescréés_technique':programmescréés_technique,'programmescréés_puissance':programmescréés_puissance,'programmescréés_endurance':programmescréés_endurance,'programmescréés_autre':programmescréés_autre})

def programme_détails(request,id,utilisateur_id) :
    programme=Programme.objects.get(id=id) #pour donner les détails d'un programme en particulier
    utilisateur=Utilisateur.objects.get(id=utilisateur_id)
    return render(request, 'monapp/programme_détails.html', {'programme': programme,'utilisateur':utilisateur})


def ajouter_activité_programme(request,id, utilisateur_id) :
    programme_utilisé= Programme.objects.get(id=id)
    utilisateur=Utilisateur.objects.get(id=utilisateur_id)
    if request.method =='POST' :
        form =Ajouter_activitéprogramme_form(request.POST)
        if form.is_valid() :
            activité= form.save(commit=False)   # arrêter la création de l'objet pour remplir le champ utilisateur avec l'id donnée
            activité.utilisateur= utilisateur   #lier mannuellement l'activité à un utilisateur(pas son id)
            activité.save()    # créer une nouvelle activité et la stocker dans la db
            return redirect('activité-détails',activité.id)    # redirige vers la liste d'activités de l'utilisateur
    else :
        form= Ajouter_activitéprogramme_form(initial={'programme':programme_utilisé}) 
        # méthode GET, on remplit automatiquement le champ programme avec celui utilisé

    return render(request, 'monapp/ajouter_activité.html', {'form': form})



def créer_programme(request,id) :
    utilisateur_utilisé=Utilisateur.objects.get(id=id)
    if request.method =='POST' :
        form =Créer_programme_form(request.POST)
        if form.is_valid() :
            programmecréé= form.save(commit=False)   # arrêter la création de l'objet pour remplir le champ utilisateur avec l'id donnée
            programmecréé.utilisateur= utilisateur_utilisé    #lier mannuellement le programme à un utilisateur(pas son id)
            programmecréé.save()    # créer un nouveau programme et le stocker dans la db
            return redirect('programme-détails',programmecréé.id, utilisateur_utilisé.id)    # redirige vers les détails du programme créé
    else :
        form= Créer_programme_form() # méthode GET

    return render(request, 'monapp/créer_programme.html', {'form': form})

    

def modifier_programme(request,id) :
    programmecréé = Programme.objects.get(id=id)
    if request.method =='POST' :
        form =Créer_programme_form(request.POST,instance=programmecréé) # on pré-rempli un formulaire avec un programme perso déjà existant
        if form.is_valid :
            # mettre à jour le programme créé déjà existante
            form.save() 
            # rediriger vers les détails du programme créé
            return redirect('programme-détails', programmecréé.id, programmecréé.utilisateur.id)
    else :
        form = Créer_programme_form(instance=programmecréé)

    return render(request, 'monapp/modifier_programme.html', {'form': form, 'programmecréé':programmecréé})

def supprimer_programme(request,id) :
    programmecréé= Programme.objects.get(id=id)
    utilisateur=programmecréé.utilisateur
    if request.method == 'POST' :
        # supprimer le groupe de la base de donnée
        programmecréé.delete()
        return redirect( 'liste-programmes', utilisateur.id)
    return render(request, 'monapp/supprimer_programme.html', {'programmecréé': programmecréé})







def liste_activités(request,id) :
    utilisateur=Utilisateur.objects.get(id=id)
    activités=Activité.objects.filter(utilisateur=id).order_by('-date') #ordonner du plus récent au moins récent
    
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
            return redirect('activité-détails',activité.id)    # redirige vers les détails de activités de l'utilisateur
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
