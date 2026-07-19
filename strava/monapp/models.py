from django.db import models
from datetime import date
from datetime import timedelta
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser,BaseUserManager




class Utilisateur(AbstractUser):
   profile_photo=models.ImageField(null=True, verbose_name='Photo de profil',blank=True)
   


        


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
    description= models.fields.CharField(max_length=500)
    nombre_exercices=models.fields.IntegerField(null=True, blank=True)
    durée=models.DurationField(validators=[validate_max_duration],default=timedelta(hours=2))
    utilisateur=models.ForeignKey(Utilisateur,null=True, on_delete=models.CASCADE)
    def __str__(self) :
        return f'{self.titre}'
    





    




class Activité(models.Model) :
    description= models.fields.CharField(max_length=500)
    date= models.DateField(auto_now_add=True) # donne automatiquement la date actuelle
    class But(models.TextChoices) :
        Technique='Technique'
        Endurance='Endurance'
        Puissance='Puissance' 
        Autre='Autre'       
        Grimpe_libre='Grimpe libre'
    but = models.fields.CharField(choices=But.choices, default='Grimpe libre')
    programme=models.ForeignKey(Programme, null=True, blank=True, on_delete=models.SET_NULL) 
    # null pour la base de donnée et blank pour le formulaire(champ pas nécessaire)
    utilisateur=models.ForeignKey(Utilisateur,default=0, on_delete=models.CASCADE)
    durée=models.DurationField(validators=[validate_max_duration],default=timedelta(hours=3)) 
    def __str__(self) :
        return f'Activité du {self.date}'
    
        
    




class Programmeechauffement(models.Model) :
    titre=models.CharField(max_length=50)
    description=models.fields.CharField(max_length= 500)
    def __str__(self):
        return f'{self.titre}'


class Photo(models.Model) :
    utilisateur=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    image=models.ImageField()
    date= models.DateField(auto_now_add=True)
    activite_liee=models.ForeignKey(Activité,on_delete=models.SET_NULL, null=True)

class Utilisateurabonnements(models.Model) :
    follower=models.ForeignKey(Utilisateur, related_name="following", on_delete=models.CASCADE)
    following=models.ForeignKey(Utilisateur, related_name="followers", on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[models.UniqueConstraint(fields=["follower","following"], name="unique_follow")]
        # pour faire en sorte qu'un utilisateur ne puisse pas s'abonner plusieurs fois à un autre (objet unique)
    
    





# Create your models here.
