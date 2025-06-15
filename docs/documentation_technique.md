# Documentation Technique

## Introduction
Ce document fournit une vue d'ensemble technique de l'application de gestion de bibliothèque. Il est destiné aux développeurs et aux administrateurs système qui doivent comprendre, configurer et maintenir l'application.

## Structure du Projet
Le projet est structuré en plusieurs modules principaux :

- `main.py` : Point d'entrée de l'application.
- `models/` : Contient les classes représentant les données de l'application.
  - `livre.py` : Modèle pour les livres.
  - `adherent.py` : Modèle pour les adhérents.
  - `emprunt.py` : Modèle pour les emprunts.
- `views/` : Contient les classes pour l'interface utilisateur.
  - `livre_view.py` : Vue pour les opérations sur les livres.
  - `adherent_view.py` : Vue pour les opérations sur les adhérents.
  - `emprunt_view.py` : Vue pour les opérations sur les emprunts.
- `controllers/` : Contient les classes pour la logique métier.
  - `livre_controller.py` : Contrôleur pour les livres.
  - `adherent_controller.py` : Contrôleur pour les adhérents.
  - `emprunt_controller.py` : Contrôleur pour les emprunts.
- `database/` : Contient les classes pour la gestion de la base de données.
  - `database_manager.py` : Gestionnaire de la base de données SQLite.

## Technologies Utilisées
- **Langage de Programmation** : Python 3.10+
- **Interface Graphique** : Tkinter
- **Base de Données** : SQLite

## Configuration et Exécution
1. **Prérequis** :
   - Assurez-vous d'avoir Python 3.10 ou une version ultérieure installée sur votre machine.
   - Installez les bibliothèques nécessaires avec `pip install -r requirements.txt` (si un fichier requirements.txt est fourni).

2. **Exécution de l'Application** :
   - Naviguez jusqu'au répertoire racine du projet.
   - Exécutez la commande `python main.py` pour démarrer l'application.

## Base de Données
L'application utilise une base de données SQLite pour stocker les informations sur les livres, les adhérents et les emprunts. La base de données est créée automatiquement lors de la première exécution de l'application.

## Architecture
L'application suit une architecture MVC (Modèle-Vue-Contrôleur) pour séparer les préoccupations et faciliter la maintenance et l'extensibilité.

## Contact
Pour toute question ou problème technique, veuillez contacter l'équipe de développement à l'adresse suivante : support@bibliotheque.com.
