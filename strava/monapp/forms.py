from django import forms
from monapp.models import Activité,Programme, Photo
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
class Ajouter_activité_form(forms.ModelForm) :
    class Meta :
        model=Activité
        exclude=('utilisateur','programme',)# on supprime ce champ du formulaire pour le remplir dans la view apres
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}
        


class Créer_programme_form(forms.ModelForm):
    class Meta :
        model=Programme
        exclude=('utilisateur',)
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}


class Ajouter_activitéprogramme_form(forms.ModelForm) :
    class Meta :
        model=Activité
        exclude=('utilisateur','programme',)
        # on supprime lee champ utilidateur du formulaire pour le remplir dans la view apres
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}
        


class LoginForm(forms.Form):
    username=forms.CharField(max_length=63,label='Identifiant') 
    password=forms.CharField(max_length=63,widget=forms.PasswordInput,label='Mot de passe')


class SignupForm(UserCreationForm) :
    class Meta(UserCreationForm.Meta) :
        model=get_user_model()
        fields=('username','email','first_name','last_name')

class UploadProfileForm(forms.ModelForm):
    class Meta :
        model=get_user_model()
        fields=('profile_photo','username',)
    
class AjouterPhotoForm(forms.ModelForm) :
    class Meta :
        model=Photo
        fields=('image',)








