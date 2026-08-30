# Strava.grimpe

Comme son nom l'indique, Strava.grimpe est un site dont le fonctionnement se rapproche de celle de l'application Strava, créé donc pour l'escalade.

## Fonctionnalités

- La première fonctionnalité principale est la création l'enregistrement d'activités dans une liste ordonnées par date de publication. Ces activités contiennent une description, un but (selon ce que l'on veut tirer de l'entraînement, comme la puissance, l'endurance etc), un durée ainsi qu'un programme ou des photos ( les deux facultatifs ).

- La seconde est la création de programmes. Certains programmes seront proposés par défaut et l'utilisateur pourra en créer lui-même. Ces programmes sont constitués d'un titre, d'une description, d'un but, d'une durée et éventuellement d'un nombre d'exercices

- La dernière fonctionnalité est la base du succès de l'application Strava. En effet, il est possible de suivre d'autres utilisateurs, ayant donc alors accès aux programmes d'entraînement qu'ils ont crées ainsi qu'à leurs activités. Il est donc possible de naviguer librement sur le compte d'un autre utilisateur lorsque'on est abonné à lui (il n'est tout de même pas possible de créer des programmes ou des activités à sa place, tout comme il n'est pas possible d'en modifier ou supprimer).

## Prérequis

Voici ce dont vous aurez besoin pour installer mon projet :

- **Python** (La version 3.13.14 ou une plus récente)
- **Django** 
- **Un environnement virtuel**
- **pip**(gère les paquets)

## Installation des prérequis

Suivez ces étapes une par une afin d'installer mon site

### 1.Clonage du code

```bash
git clone https://github.com/Camilleeigenmann/monsite.git
cd monsite
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
venv\Scripts\activate
```

### 3. Installation de Django

```bash
pip install django
```

### 4. Stockage des paquets

```bash
pip install -r requirements.txt
```

### 5. Lancement du site

```bash
cd strava
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Outils

-**Python**
-[**Django**](https://docs.djangoproject.com/en/6.0/)


