from django import forms
from monapp.models import Activité,Programme
from django.core.exceptions import ValidationError
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
        exclude=('utilisateur',)
        # on supprime ce champ du formulaire pour le remplir dans la view apres
        widgets={'description': forms.Textarea(attrs={'rows':5,'cols':50})}
        def __init__(self, *args, **kwargs) :
            super().__init__(*args,**kwargs)
            #rend le champ programme inchangeable car on va introduire le programme ayant appelé ce formulaire
            self.fields['programme'].disabled = True


        







