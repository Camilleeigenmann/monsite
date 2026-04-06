from django import forms
from monapp.models import Activité,ProgrammeCréé
class Ajouter_activité_form(forms.ModelForm) :
    class Meta :
        model=Activité
        exclude=('utilisateur',)# on supprime ce champ du formulaire pour le remplir dans la view apres

class Créer_programme_form(forms.ModelForm):
    class Meta :
        model=ProgrammeCréé
        exclude=('utilisateur',)