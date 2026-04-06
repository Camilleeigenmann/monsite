"""
URL configuration for strava project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from monapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/',views.accueil),
    path('',views.accueil),
    
    path('<int:id>/programmes/', views.liste_programmes, name="liste-programmes"),
    path('programmes/<int:id>/', views.programme_détails, name="programme-détails"),

    path('programmescréés/<int:id>/', views.programmecréé_détails,name="programmecréé-détails"),
    path('programmescréés/créer/<int:id>/', views.créer_programme, name="créer-programme"),
    path('programmescréés/modifier/<int:id>/', views.modifier_programme,name="modifier-programme"),
    path('programmescréés/supprimer/<int:id>/', views.supprimer_programme,name="supprimer-programme"),

    path('<int:id>/activités/', views.liste_activités, name="liste-activités"),
    path('activités/<int:id>/', views.activité_détails, name="activité-détails"),
    path('activités/ajouter/<int:id>/',views.ajouter_activité,name="ajouter-activité"),
    path('activités/modifier/<int:id>/', views.modifier_activité, name="modifier-activité"),
    path('activités/supprimer/<int:id>/', views.supprimer_activité, name="supprimer-activité"),

]
