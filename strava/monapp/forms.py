from django import forms
from monapp.models import Activité,ProgrammeCréé
from django.core.exceptions import ValidationError
class Ajouter_activité_form(forms.ModelForm) :
    class Meta :
        model=Activité
        exclude=('utilisateur','programmecréé',)# on supprime ce champ du formulaire pour le remplir dans la view apres
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}
        


class Créer_programme_form(forms.ModelForm):
    class Meta :
        model=ProgrammeCréé
        exclude=('utilisateur',)
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}


class Ajouter_activitéprogrammecréé_form(forms.ModelForm) :
    class Meta :
        model=Activité
        exclude=('utilisateur','programme',)
        # on supprime ce champ du formulaire pour le remplir dans la view apres
        # on supprime aussi le champ programme car on ne peut de toute façon pas utiliser deux programmes
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}
        def __init__(self, *args, **kwargs) :
            super().__init__(*args,**kwargs)
            #rend le champ programmecréé inchangeable car on va introduire le programme ayant appelé ce formulaire
            self.fields['programme'].readonly=True


        







