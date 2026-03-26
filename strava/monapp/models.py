from django.db import models
class Utilisateur(models.Model):
    identifiant=models.fields.CharField(max_length=10)
    email= models.fields.EmailField(max_length= 100)
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
class Activité(models.Model) :
    description= models.fields.CharField(max_length=400)
    date= models.DateField()
    programme=models.ForeignKey(Programme, null=True, on_delete=models.SET_NULL)
    
class Programmeechauffement(models.Model) :
    
    description=models.fields.CharField(max_length= 400)








# Create your models here.
