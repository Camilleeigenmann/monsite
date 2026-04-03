from django.db import models
from datetime import date
from datetime import timedelta
from django.core.validators import MaxValueValidator
class Utilisateur(models.Model):
    nom=models.fields.CharField( max_length=20)
    prénom=models.fields.CharField(max_length=20)
    def __str__(self) :
        return f'{self.prénom} {self.nom}'

def validate_max_duration(value) :
    if value.total_seconds() > 6 * 3600 :
        raise ValidationError("La durée ne peut pas dépasser 6h") # donne un maximum de 6h aux programmes et à l'activité

class Programme(models.Model) :
    titre= models.CharField(max_length=30)
    class But(models.TextChoices) :
        Technique='Technique'
        Endurance='Endurance'
        Puissance='Puissance'        
        Grimpe_libre= 'Grimpe libre'
    but = models.fields.CharField(choices=But.choices)
    description= models.fields.CharField(max_length=400)
    nombre_exercices=models.fields.IntegerField(null=True)
    durée=models.DurationField(validators=[validate_max_duration],default=timedelta(hours=2))
    def __str__(self) :
        return f'{self.titre}'
    

class Activité(models.Model) :
    description= models.fields.CharField(max_length=500)
    date= models.DateField(auto_now_add=True)
    programme=models.ForeignKey(Programme, null=True, on_delete=models.SET_NULL)
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
