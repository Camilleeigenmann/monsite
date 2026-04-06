from django.db import models
from datetime import date
from datetime import timedelta
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

class Utilisateur(models.Model):
    nom=models.fields.CharField( max_length=20)
    prénom=models.fields.CharField(max_length=20)
    def __str__(self) :
        return f'{self.prénom} {self.nom}'


        


def validate_max_duration(value) :
        if value.total_seconds() > 8 * 3600 :
            raise ValidationError("La durée ne peut pas dépasser 8h") # donne un maximum de 8h aux programmes et à l'activité




class Programme(models.Model) :
    titre= models.CharField(max_length=30)
    class But(models.TextChoices) :
        Technique='Technique'
        Endurance='Endurance'
        Puissance='Puissance'        
        Autre='Autre'
    but = models.fields.CharField(choices=But.choices)
    description= models.fields.CharField(max_length=400)
    nombre_exercices=models.fields.IntegerField(null=True, blank=True)
    durée=models.DurationField(validators=[validate_max_duration],default=timedelta(hours=2))
    def __str__(self) :
        return f'{self.titre}'
    




class ProgrammeCréé(models.Model) :
    titre= models.CharField(max_length=30)
    class But(models.TextChoices) :
        Technique='Technique'
        Endurance='Endurance'
        Puissance='Puissance'        
        Autre='Autre'
    but = models.fields.CharField(choices=But.choices)
    utilisateur=models.ForeignKey(Utilisateur,default=0, on_delete=models.CASCADE)
    description= models.fields.CharField(max_length=400)
    nombre_exercices=models.fields.IntegerField(null=True,blank=True)
    durée=models.DurationField(validators=[validate_max_duration],default=timedelta(hours=2))
    def __str__(self) :
        return f'{self.titre}'
    




class Activité(models.Model) :
    description= models.fields.CharField(max_length=500)
    date= models.DateField(auto_now_add=True) # donne automatiquement la date actuelle
    class But(models.TextChoices) :
        Technique='Technique'
        Endurance='Endurance'
        Puissance='Puissance'        
        Grimpe_libre='Grimpe libre'
    but = models.fields.CharField(choices=But.choices, default='Grimpe libre')
    programme=models.ForeignKey(Programme, null=True, blank=True, on_delete=models.SET_NULL) 
    # null pour la base de donnée et blank pour le formulaire(champ pas nécessaire)
    programmecréé=models.ForeignKey(ProgrammeCréé, null=True, blank=True, on_delete=models.SET_NULL)
    utilisateur=models.ForeignKey(Utilisateur,default=0, on_delete=models.CASCADE)
    durée=models.DurationField(validators=[validate_max_duration],default=timedelta(hours=3)) 
    def __str__(self) :
        return f'Activité du {self.date}'

    




class Programmeechauffement(models.Model) :
    titre=models.CharField(max_length=50)
    description=models.fields.CharField(max_length= 500)
    def __str__(self):
        return f'{self.titre}'









# Create your models here.
