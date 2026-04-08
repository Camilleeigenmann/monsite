from django import forms
from monapp.models import Activité,ProgrammeCréé
from django.core.exceptions import ValidationError
class Ajouter_activité_form(forms.ModelForm) :
    class Meta :
        model=Activité
        exclude=('utilisateur',)# on supprime ce champ du formulaire pour le remplir dans la view apres
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}
        


class Créer_programme_form(forms.ModelForm):
    class Meta :
        model=ProgrammeCréé
        exclude=('utilisateur',)
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}


