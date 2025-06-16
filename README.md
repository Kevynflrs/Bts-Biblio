# Application de Gestion de Bibliothèque

Une application client lourd pour la gestion d'une bibliothèque, permettant d'enregistrer, consulter, modifier et supprimer des ouvrages, ainsi que de gérer les adhérents et les emprunts.

## Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Installation des dépendances](#Installation des Dépendances)
- [Exécution](#exécution)
- [Structure du Projet](#structure-du-projet)
- [Documentation](#documentation)

## Fonctionnalités

- **Gestion des Livres** : Ajout, modification, suppression et recherche de livres.
- **Gestion des Adhérents** : Ajout, modification, suppression et recherche d'adhérents.
- **Gestion des Emprunts** : Enregistrement des emprunts et des retours de livres.
- **Interface Graphique** : Interface simple et intuitive avec Tkinter.
- **Base de Données** : Persistance des données avec une base de données SQLite.

## Prérequis

- Python 3.10 ou supérieur
- Tkinter (généralement inclus avec Python)
- SQLite3 (généralement inclus avec Python)

## Installation

1. Clonez le dépôt du projet sur votre machine locale :

   git clone https://github.com/Kevynflrs/Bts-Biblio.git

2. Naviguez dans le répertoire du projet :
    
    cd Bts-Biblio

3. (Optionnel) Créez et activez un environnement virtuel :

    python -m venv venv
    source venv/bin/activate  # Sur Linux/Mac
    .\venv\Scripts\activate  # Sur Windows

## Installation des Dépendances

Avant de pouvoir exécuter l'application, vous devez installer les dépendances nécessaires. Vous pouvez le faire en utilisant `pip`, le gestionnaire de paquets de Python. Ouvrez un terminal ou une invite de commandes et exécutez les commandes suivantes :

    pip install pandas matplotlib pyinstaller

Ces commandes installeront les bibliothèques nécessaires pour exécuter l'application, notamment :

    Pandas : Utilisé pour la manipulation et l'analyse des données.
    Matplotlib : Utilisé pour la visualisation des données et la création de graphiques.
    PyInstaller : Utilisé pour créer des exécutables à partir de scripts Python.


## Installation

Pour démarrer l'application, exécutez le fichier main.py :

    python main.py

## Structure du Projet

projet_bibliotheque/
│
├── main.py                  # Point d'entrée de l'application
├── models/                  # Modèles de données
│   ├── __init__.py
│   ├── livre.py
│   ├── adherent.py
│   └── emprunt.py
├── views/                   # Vues de l'interface utilisateur
│   ├── __init__.py
│   ├── livre_view.py
│   ├── adherent_view.py
│   └── emprunt_view.py
├── controllers/             # Contrôleurs pour la logique métier
│   ├── __init__.py
│   ├── livre_controller.py
│   ├── adherent_controller.py
│   └── emprunt_controller.py
├── database/                # Gestion de la base de données
│   ├── __init__.py
│   └── database_manager.py
└── docs/                    # Documentation technique et utilisateur
    ├── documentation_technique.md
    └── documentation_utilisateur.md

## Documentation

Pour plus de détails sur l'utilisation et la configuration de l'application, consultez la documentation dans le dossier docs/.

