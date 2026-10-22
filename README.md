# Grimp'mania

Grimp'mania est un site conçu spécialement pour l'escalade, permettant aux utilisateurs de suivre leurs entraînements et de partager leurs activités ou leurs programmes avec leurs abonnés.

## Fonctionnalités

- La première fonctionnalité principale est la création et l'enregistrement d'activités dans une liste ordonnées par date de publication. Ces activités contiennent une description, un but (selon ce que l'on veut tirer de l'entraînement, comme la puissance, l'endurance etc), une durée ainsi qu'un programme ou des photos ( les deux facultatifs ).

- La seconde est la création de programmes. Certains programmes seront proposés par défaut et l'utilisateur pourra en créer lui-même. Ces programmes sont constitués d'un titre, d'une description, d'un but, d'une durée et éventuellement d'un nombre d'exercices

- La dernière fonctionnalité est la base du succès de l'application Strava. En effet, il est possible de suivre d'autres utilisateurs, ayant donc alors accès aux programmes d'entraînement qu'ils ont crées ainsi qu'à leurs activités. Il est donc possible de naviguer librement sur le compte d'un autre utilisateur lorsque'on est abonné à lui (il n'est tout de même pas possible de créer des programmes ou des activités à sa place, tout comme il n'est pas possible d'en modifier ou supprimer).

## Prérequis

Voici ce dont vous aurez besoin pour installer mon projet :

- **Python** (La version 3.13.14 ou une plus récente)
- **Django** (J'ai utilisé la versin 6.0.4)
- **Un environnement virtuel**
- **pip**(gère les paquets et est normalement inclus en installant Python)
-**Pillow**(pour ajouter des photos sur le site)

## Installation des prérequis

Suivez ces étapes une par une afin d'installer mon site

### 0.1 Installation de Python et de pip

Avant de démarrer le code, vérifiez que Python est bien installé et que pip est bien inclus dedans.
```bash
python --version
pip --version
```
Si cette première ligne ne fonctionne pas, alors tapez la suivante :
```bash
python3 --version
```
### 1.Clonage du code

```bash
git clone https://github.com/Camilleeigenmann/monsite.git
cd strava 
```

### 2. Création de l'environnement virtuel puis activation

Sur macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
Sur Windows
```bash
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Installation de Django

```bash
python -m pip install Django
```
Puis vérifiez que celui ci est bien installé en tapant une de ces lignes:
```bash
django-admin --version
```
ou 
```bash
python -m django --version
```
### 4. Installation de Pillow
```bash
pip install Pillow
```

### 5. Lancement du site

```bash
cd strava
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Le site sera accessible à :
```bash
http://127.0.0.1:8000/
```

## Administration
Pour accéder à l'administration Django :
```bash
python manage.py createsuperuser
```
Puis rendez-vous sur:
```bash
http://127.0.0.1:8000/admin/
```


## Outils

-**Python**
-[**Django**](https://docs.djangoproject.com/en/6.0/)
-**HTML**
-[**W3.CSS**](https://www.w3schools.com/w3css/)

## Auteur

Site créé par Camille Eigenmann