from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponse, redirect
from monapp.models import Utilisateur,Programme,Programmeechauffement,Activité,Photo, Utilisateurabonnements
from . import forms
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

def signup(request) :
    form=forms.SignupForm()
    if request.method=='POST':
        form =forms.SignupForm(request.POST)
        if form.is_valid :
            utilisateur=form.save()
            login(request,utilisateur)
            return redirect(settings.LOGIN_REDIRECT_URL,utilisateur.id)

    return render(request, 'monapp/signup.html', {'form':form})



def logout_utilisateur(request) :
    logout(request)
    return redirect('login')




def login_page(request):
    form=forms.LoginForm()
    
    if request.method == 'POST':
        form=forms.LoginForm(request.POST)
        if form.is_valid() :
            utilisateur=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if utilisateur is not None :
                login(request,utilisateur)
                return redirect('accueil-utilisateur',utilisateur.id)

    return render(request,'monapp/login.html',{'form':form})

@login_required
def upload_profile(request,id):
    user=request.user
    utilisateur=Utilisateur.objects.get(id=id)
    form=forms.UploadProfileForm(instance=utilisateur)
    if request.method=='POST' :
        form=forms.UploadProfileForm(request.POST,request.FILES, instance=utilisateur)
        if form.is_valid:
            form.save()
            return redirect('accueil-utilisateur', id)
    return render(request, 'monapp/upload_profile.html',{'form':form, 'utilisateur':utilisateur,'user':user})


def ajouter_photo(request,id) :
    user=request.user
    utilisateur=Utilisateur.objects.get(id=id)
    if request.method=='POST':
        form=forms.AjouterPhotoForm(request.POST, request.FILES)
        if form.is_valid:
            photo=form.save(commit=False)
            photo.utilisateur=utilisateur
            photo.save()
            return redirect('accueil-utilisateur', utilisateur.id)
    else :
        form=forms.AjouterPhotoForm()
    
    return render(request, 'monapp/ajouter_photo.html', {'utilisateur':utilisateur,'form':form,'user':user})


@login_required
def accueil_utilisateur(request, id ):
    user=request.user
    utilisateur=Utilisateur.objects.get(id=user.id)

    abonnements=utilisateur.following.all().count()
    abonnes=utilisateur.followers.all().count()
    abonnements_ids=utilisateur.following.all()
    abonnes_ids=utilisateur.followers.all()
    abonnements_dt=[]
    abonnes_dt=[]

    for abonne in abonnes_ids :
        abonnes_dt.append(abonne.follower)
    for abonnement in abonnements_ids :
        abonnements_dt.append(abonnement.following)



    now=timezone.now()
    mois_actuel=now.month
    annee_actuelle=now.year
    
    activites_utilisateur=Activité.objects.filter(utilisateur_id=utilisateur.id)
    derniere_activite=activites_utilisateur.order_by('-date').first() #sélectionner la dernière activité

    activites_du_mois=Activité.objects.filter(utilisateur_id=utilisateur.id,date__year=now.year,date__month=now.month)
    #prends uniquement les activités créées le mois se déroulant actuellement grâce à timezone.now().month/year
    # et date__year/date__month
    duree_totale_mois=activites_du_mois.aggregate(total=Sum('durée'))['total']
    #fais la somme de la durée des activités du mois 

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
    #filtrer les activités du mois en fonction de leurs buts pour donner un résumé plus qualitatif
    

    activites_annee=Activité.objects.filter(utilisateur_id=utilisateur.id,date__year=now.year)
    #prends uniquement les activités de l'année actuelle grâce à date__year et timezone.now()
    duree_totale_annee=activites_annee.aggregate(total=Sum('durée'))['total']

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
    

    photos=Photo.objects.filter(utilisateur_id=utilisateur.id).order_by('-date') #recupere les photos liées à l'utilisateur en question



    return render(request,'monapp/accueil_utilisateur.html', {'utilisateur':utilisateur,'user':user
    ,'abonnements':abonnements, 'abonnes':abonnes,'abonnements_dt':abonnements_dt,'abonnes_dt':abonnes_dt
    ,'mois_actuel':mois_actuel,'annee_actuelle':annee_actuelle, 'photos':photos
    ,'derniere_activite':derniere_activite, 'activites_utilisateur':activites_utilisateur
    ,'activites_du_mois':activites_du_mois,'activites_annee':activites_annee
    ,'duree_totale_mois' :duree_totale_mois,'duree_totale_annee':duree_totale_annee
    ,'nb_activites_technique_mois':nb_activites_technique_mois, 'nb_activites_puissance_mois':nb_activites_puissance_mois
    ,'nb_activites_endurance_mois':nb_activites_endurance_mois,'nb_activites_autre_mois':nb_activites_autre_mois
    ,'nb_activites_grimpe_libre_mois':nb_activites_grimpe_libre_mois
    ,'nb_activites_technique_annee':nb_activites_technique_annee,'nb_activites_puissance_annee':nb_activites_puissance_annee
    ,'nb_activites_endurance_annee':nb_activites_endurance_annee,'nb_activites_autre_annee':nb_activites_autre_annee
    ,'nb_activites_grimpe_libre_annee':nb_activites_grimpe_libre_annee})


def liste_utilisateurs(request):
    utilisateurs= Utilisateur.objects.all().order_by('username')
    user=request.user
    utilisateur=Utilisateur.objects.get(id=user.id)
    suivis=[]
    nonsuivis=[]
    for grimpeur in utilisateurs :
        if Utilisateurabonnements.objects.filter(follower=utilisateur.id, following=grimpeur.id).exists() :
            suivis.append(grimpeur)
        else:
            nonsuivis.append(grimpeur)


    return render(request, 'monapp/liste_utilisateurs.html', {'utilisateur': utilisateur,'user':user,'suivis':suivis ,'nonsuivis':nonsuivis})


def abonner(request, id):
    utilisateur_cible= Utilisateur.objects.get(id=id)
    user=request.user
    utilisateur=Utilisateur.objects.get(id=user.id)
    if utilisateur != utilisateur_cible :
        Utilisateurabonnements.objects.create(follower=utilisateur, following=utilisateur_cible)

    utilisateurs= Utilisateur.objects.all().order_by('username')
    suivis=[]
    nonsuivis=[]
    for grimpeur in utilisateurs :
        if Utilisateurabonnements.objects.filter(follower=utilisateur.id, following=grimpeur.id).exists() :
            suivis.append(grimpeur)
        else:
            nonsuivis.append(grimpeur)


    return render(request, 'monapp/liste_utilisateurs.html', {'utilisateur': utilisateur,'user':user, 'suivis':suivis ,'nonsuivis':nonsuivis})
    

def desabonner(request, id) :
    utilisateur_cible= Utilisateur.objects.get(id=id)
    user= request.user
    utilisateur=Utilisateur.objects.get(id=user.id)
    Utilisateurabonnements.objects.filter(follower=utilisateur.id, following=utilisateur_cible.id ).delete()

    utilisateurs= Utilisateur.objects.all().order_by('username')
    suivis=[]
    nonsuivis=[]
    for grimpeur in utilisateurs :
        if Utilisateurabonnements.objects.filter(follower=utilisateur.id, following=grimpeur.id).exists() :
            suivis.append(grimpeur)
        else:
            nonsuivis.append(grimpeur)


    return render(request, 'monapp/liste_utilisateurs.html', {'utilisateur': utilisateur,'user':user,'suivis':suivis,'nonsuivis':nonsuivis})


def profil_utilisateur(request, id) :
    user= request.user
    utilisateur=Utilisateur.objects.get(id=user.id)
    utilisateur_cible=Utilisateur.objects.get(id=id)
    if Utilisateurabonnements.objects.filter(follower=utilisateur.id, following=utilisateur_cible.id).exists():
        suivi=True
    else:
        suivi=False
    
    abonnes=utilisateur_cible.followers.all().count()
    abonnements=utilisateur_cible.following.all().count()

    programmes=Programme.objects.filter(utilisateur=utilisateur_cible.id)
    programmes_technique=Programme.objects.filter(but='Technique', utilisateur=utilisateur_cible.id)
    programmes_puissance=Programme.objects.filter(but='Puissance', utilisateur=utilisateur_cible.id)
    programmes_endurance=Programme.objects.filter(but='Endurance', utilisateur=utilisateur_cible.id)
    programmes_autre=Programme.objects.filter(but='Autre', utilisateur=utilisateur_cible.id)

    return render(request, 'monapp/profil_utilisateur.html', {'utilisateur':utilisateur,'user':user
    ,'utilisateur_cible':utilisateur_cible, 'suivi':suivi
    ,'abonnes':abonnes, 'abonnements':abonnements,'programmes':programmes
    ,'programmes_technique':programmes_technique, 'programmes_puissance':programmes_puissance
    ,'programmes_endurance':programmes_endurance, 'programmes_autre':programmes_autre})



@login_required
def liste_programmes(request,id):
    user=request.user
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
    
    return render(request, 'monapp/liste_programmes.html', {'programmes':programmes, 'utilisateur':utilisateur,'user':user,'programmescréés':programmescréés,
    'programmes_technique':programmes_technique,'programmes_puissance':programmes_puissance,'programmes_endurance':programmes_endurance,'programmes_autre':programmes_autre,
    'programmescréés_technique':programmescréés_technique,'programmescréés_puissance':programmescréés_puissance,'programmescréés_endurance':programmescréés_endurance,'programmescréés_autre':programmescréés_autre})


@login_required
def programme_détails(request,id,utilisateur_id) :
    programme=Programme.objects.get(id=id) #pour donner les détails d'un programme en particulier
    utilisateur=Utilisateur.objects.get(id=utilisateur_id)
    user=request.user
    return render(request, 'monapp/programme_détails.html', {'programme': programme,'utilisateur':utilisateur,'user':user})



def ajouter_activité_photo(request, id, utilisateur_id):
    user=request.user
    activite=Activité.objects.get(id=id)
    utilisateur=Utilisateur.objects.get(id=utilisateur_id)
    if request.method=='POST' :
        form=forms.AjouterPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo=form.save(commit=False)
            photo.utilisateur=utilisateur
            photo.activite_liee=activite
            photo.save()
            return redirect('activité-détails',activite.id)
    else :
        form=forms.AjouterPhotoForm()
    
    return render(request, 'monapp/ajouter_photo.html', {'form':form, 'utilisateur':utilisateur,'activite':activite,'user':user})



@login_required
def ajouter_activité_programme(request,id, utilisateur_id) :
    user=request.user
    programme_utilisé= Programme.objects.get(id=id)
    utilisateur=Utilisateur.objects.get(id=utilisateur_id)
    if request.method =='POST' :
        form =forms.Ajouter_activitéprogramme_form(request.POST)
        if form.is_valid() :
            activité= form.save(commit=False)   # arrêter la création de l'objet pour remplir le champ utilisateur avec l'id donnée
            activité.utilisateur= utilisateur   #lier mannuellement l'activité à un utilisateur(pas son id)
            activité.programme=programme_utilisé #lier manuellement à l'activité
            activité.save()    # créer une nouvelle activité et la stocker dans la db
            return redirect('activité-détails',activité.id)    # redirige vers la liste d'activités de l'utilisateur
    else :
        form= forms.Ajouter_activitéprogramme_form() 
        # 

    return render(request, 'monapp/ajouter_activité.html', {'form': form, 'utilisateur':utilisateur,'user':user,'programme_utilisé':programme_utilisé})



@login_required
def créer_programme(request,id) :
    user=request.user
    utilisateur_utilisé=Utilisateur.objects.get(id=id)
    if request.method =='POST' :
        form =forms.Créer_programme_form(request.POST)
        if form.is_valid() :
            programmecréé= form.save(commit=False)   # arrêter la création de l'objet pour remplir le champ utilisateur avec l'id donnée
            programmecréé.utilisateur= utilisateur_utilisé    #lier mannuellement le programme à un utilisateur(pas son id)
            programmecréé.save()    # créer un nouveau programme et le stocker dans la db
            return redirect('programme-détails',programmecréé.id, utilisateur_utilisé.id)    # redirige vers les détails du programme créé
    else :
        form= forms.Créer_programme_form() # méthode GET

    return render(request, 'monapp/créer_programme.html', {'form': form, 'utilisateur':utilisateur_utilisé,'user':user})

    

@login_required
def modifier_programme(request,id) :
    user=request.user
    programmecréé = Programme.objects.get(id=id)
    utilisateur=programmecréé.utilisateur
    if request.method =='POST' :
        form =forms.Créer_programme_form(request.POST,instance=programmecréé) # on pré-rempli un formulaire avec un programme perso déjà existant
        if form.is_valid :
            # mettre à jour le programme créé déjà existante
            form.save() 
            # rediriger vers les détails du programme créé
            return redirect('programme-détails', programmecréé.id, programmecréé.utilisateur.id)
    else :
        form = forms.Créer_programme_form(instance=programmecréé)

    return render(request, 'monapp/modifier_programme.html', {'form': form, 'programmecréé':programmecréé, 'utilisateur':utilisateur,'user':user})

@login_required
def supprimer_programme(request,id) :
    user=request.user
    programmecréé= Programme.objects.get(id=id)
    utilisateur=programmecréé.utilisateur
    if request.method == 'POST' :
        # supprimer le groupe de la base de donnée
        programmecréé.delete()
        return redirect( 'liste-programmes', utilisateur.id)
    return render(request, 'monapp/supprimer_programme.html', {'programmecréé': programmecréé, 'utilisateur':utilisateur,'user':user})






@login_required
def liste_activités(request,id) :
    user=request.user
    utilisateur=Utilisateur.objects.get(id=id) #user et utilisateur pour pouvorr mettre des restrictions si le user est un abonné
    #-> donc pas de possibilité d'ajouter des activités sur ce profil ou de modifier les activités
    activités=Activité.objects.filter(utilisateur=id).order_by('-date') #ordonner du plus récent au moins récent
    
# les activités liés à cet utilisateur seront donc séléctionnées puis affichées (un seul dictionnaire sinon ça bug)
    return render(request, 'monapp/liste_activités.html', {'activités':activités , 'utilisateur': utilisateur,'user':user})


@login_required
def liste_activites_abo(request,id) :
    utilisateur=Utilisateur.objects.get(id=id)
    user=request.user
    abonnements=user.following.all()
    activites=[]
    for utilisateur in abonnements :
        activites_utilisateur=Activité.objects.filter(utilisateur=utilisateur.id)
        activites.extend(activites_utilisateur)
    activites=sorted(activites, key=lambda x: x.date, reverse=True)

    return render(request, 'monapp/liste_activites_abo.html', {'user':user,'activites':activites})



@login_required
def activité_détails(request,id):
    activité=Activité.objects.get(id=id)
    programme=activité.programme
    user=request.user
    utilisateur=activité.utilisateur #même chose qu'en haut
    photos=Photo.objects.filter(utilisateur_id=utilisateur.id, activite_liee_id=activité.id).order_by('-date')


    return render(request,'monapp/activité_détails.html', {'activité':activité, 'programme':programme , 'utilisateur':utilisateur,
    'photos':photos, 'user':user})

@login_required
def ajouter_activité(request,id) :
    user=request.user
    utilisateur_utilisé=Utilisateur.objects.get(id=id)
    if request.method =='POST' :
        form =forms.Ajouter_activité_form(request.POST)
        if form.is_valid() :
            activité= form.save(commit=False)   # arrêter la création de l'objet pour remplir le champ utilisateur avec l'id donnée
            activité.utilisateur= utilisateur_utilisé    #lier mannuellement l'activité à un utilisateur(pas son id)
            activité.save()    # créer une nouvelle activité et la stocker dans la db
            return redirect('activité-détails',activité.id)    # redirige vers les détails de activités de l'utilisateur
    else :
        form= forms.Ajouter_activité_form() # méthode GET

    return render(request, 'monapp/ajouter_activité.html', {'form': form,'utilisateur':utilisateur_utilisé,'user':user})

@login_required
def modifier_activité(request,id) :
    user=request.user
    activité = Activité.objects.get(id=id)
    utilisateur=activité.utilisateur
    if request.method =='POST' :
        form =forms.Ajouter_activité_form(request.POST,instance=activité) # on pré-rempli un formulaire avec une activité déjà existant
        if form.is_valid :
            # mettre à jour l'activité déjà existante
            form.save() 
            # rediriger vers les détails de l'activité
            return redirect('activité-details', activité.id)
    else :
        form = forms.Ajouter_activité_form(instance=activité)

    return render(request, 'monapp/modifier_activité.html', {'form': form, 'activité':activité, 'utilisateur':utilisateur,'user':user})

@login_required
def supprimer_activité(request,id) :
    user=request.user
    activité= Activité.objects.get(id=id)
    utilisateur=activité.utilisateur
    if request.method == 'POST' :
        # supprimer le groupe de la base de donnée
        activité.delete()
        return redirect( 'liste-activités', utilisateur.id)
    return render(request, 'monapp/supprimer_activité.html', {'activité': activité, 'utilisateur':utilisateur,'user':user})

    

# Create your views here.
