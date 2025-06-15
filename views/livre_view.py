import tkinter as tk
from tkinter import messagebox
from controllers.livre_controller import LivreController
import re

class LivreView:
    def __init__(self, root, db_file):
        """
        Initialise la vue des livres.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        """
        self.root = root
        self.livre_controller = LivreController(db_file)
        self.create_widgets()
        self.refresh_livre_list()

    def create_widgets(self):
        """Crée les widgets pour l'interface des livres."""
        # Titre
        self.label_titre = tk.Label(self.root, text="Titre")
        self.label_titre.grid(row=0, column=0)
        self.entry_titre = tk.Entry(self.root)
        self.entry_titre.grid(row=0, column=1)

        # Auteur
        self.label_auteur = tk.Label(self.root, text="Auteur")
        self.label_auteur.grid(row=1, column=0)
        self.entry_auteur = tk.Entry(self.root)
        self.entry_auteur.grid(row=1, column=1)

        # Année
        self.label_annee = tk.Label(self.root, text="Année")
        self.label_annee.grid(row=2, column=0)
        self.entry_annee = tk.Entry(self.root)
        self.entry_annee.grid(row=2, column=1)

        # Boutons
        self.button_ajouter = tk.Button(self.root, text="Ajouter", command=self.ajouter_livre)
        self.button_ajouter.grid(row=3, column=0)

        self.button_rechercher = tk.Button(self.root, text="Rechercher", command=self.rechercher_livre)
        self.button_rechercher.grid(row=3, column=1)

        self.button_lister = tk.Button(self.root, text="Lister", command=self.refresh_livre_list)
        self.button_lister.grid(row=3, column=2)

        # Zone de texte pour afficher les résultats
        self.text_results = tk.Text(self.root, height=10, width=50)
        self.text_results.grid(row=4, column=0, columnspan=3)

    def validate_input(self, titre, auteur, annee):
        """Valide les entrées utilisateur avec des expressions régulières."""
        # Vérifie que le titre et l'auteur ne contiennent que des lettres, des chiffres et des espaces
        if not re.match(r'^[a-zA-Z0-9\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', titre):
            messagebox.showerror("Erreur", "Le titre contient des caractères invalides.")
            return False

        if not re.match(r'^[a-zA-Z0-9\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', auteur):
            messagebox.showerror("Erreur", "L'auteur contient des caractères invalides.")
            return False

        # Vérifie que l'année est un nombre valide
        if not re.match(r'^\d{4}$', str(annee)):
            messagebox.showerror("Erreur", "L'année doit être un nombre à 4 chiffres.")
            return False

        return True

    def ajouter_livre(self):
        """Ajoute un livre à la base de données."""
        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        annee = self.entry_annee.get()

        if not titre or not auteur or not annee:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        try:
            annee = int(annee)
        except ValueError:
            messagebox.showerror("Erreur", "L'année doit être un nombre.")
            return

        if not self.validate_input(titre, auteur, annee):
            return

        self.livre_controller.add_livre(titre, auteur, annee)
        messagebox.showinfo("Succès", "Livre ajouté avec succès.")
        self.refresh_livre_list()

    def rechercher_livre(self):
        """Recherche des livres dans la base de données."""
        query = self.entry_titre.get()
        self.refresh_livre_list(query)

    def refresh_livre_list(self, query=""):
        """Rafraîchit la liste des livres affichée."""
        livres = self.livre_controller.search_livres(query)
        self.text_results.delete(1.0, tk.END)
        for livre in livres:
            self.text_results.insert(tk.END, f"ID: {livre[0]}, Titre: {livre[1]}, Auteur: {livre[2]}, Année: {livre[3]}\n")