from django import forms
from monapp.models import Activité
class Ajouter_activité_form(forms.ModelForm) :
    class Meta :
        model=Activité
        exclude=('utilisateur',)# on supprime ce champ du formulaire pour le remplir dans la view apres