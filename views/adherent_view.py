import tkinter as tk
from tkinter import messagebox
from controllers.adherent_controller import AdherentController
import re

class AdherentView:
    def __init__(self, root, db_file, role):
        """
        Initialise la vue des adhérents.

        Arguments :
        root : La fenêtre principale de l'application.
        db_file (str) : Le chemin vers le fichier de la base de données.
        role (str) : Le rôle de l'utilisateur (admin ou agent).
        """
        self.root = root
        self.adherent_controller = AdherentController(db_file)
        self.role = role
        self.create_widgets()
        self.refresh_adherent_list()

    def create_widgets(self):
        """Crée les widgets pour l'interface des adhérents."""
        # Nom
        self.label_nom = tk.Label(self.root, text="Nom")
        self.label_nom.grid(row=0, column=0)
        self.entry_nom = tk.Entry(self.root)
        self.entry_nom.grid(row=0, column=1)

        # Prénom
        self.label_prenom = tk.Label(self.root, text="Prénom")
        self.label_prenom.grid(row=1, column=0)
        self.entry_prenom = tk.Entry(self.root)
        self.entry_prenom.grid(row=1, column=1)

        # Email
        self.label_email = tk.Label(self.root, text="Email")
        self.label_email.grid(row=2, column=0)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=2, column=1)

        # Boutons
        self.button_ajouter = tk.Button(self.root, text="Ajouter", command=self.ajouter_adherent)
        self.button_ajouter.grid(row=3, column=0)

        self.button_rechercher = tk.Button(self.root, text="Rechercher", command=self.rechercher_adherent)
        self.button_rechercher.grid(row=3, column=1)

        self.button_lister = tk.Button(self.root, text="Lister", command=self.refresh_adherent_list)
        self.button_lister.grid(row=3, column=2)

        # Désactiver les boutons pour les agents
        if self.role != "admin":
            self.button_ajouter.config(state=tk.DISABLED)

        # Zone de texte pour afficher les résultats
        self.text_results = tk.Text(self.root, height=10, width=50)
        self.text_results.grid(row=4, column=0, columnspan=3)

    def validate_input(self, nom, prenom, email):
        """Valide les entrées utilisateur avec des expressions régulières."""
        if not re.match(r'^[a-zA-Z\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', nom):
            messagebox.showerror("Erreur", "Le nom contient des caractères invalides.")
            return False

        if not re.match(r'^[a-zA-Z\s\-éèêëàâäçîïôöùûüÿœæÉÈÊËÀÂÄÇÎÏÔÖÙÛÜŸŒÆ]+$', prenom):
            messagebox.showerror("Erreur", "Le prénom contient des caractères invalides.")
            return False

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messagebox.showerror("Erreur", "L'email est invalide.")
            return False

        return True

    def ajouter_adherent(self):
        """Ajoute un adhérent à la base de données."""
        nom = self.entry_nom.get()
        prenom = self.entry_prenom.get()
        email = self.entry_email.get()

        if not nom or not prenom or not email:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        if not self.validate_input(nom, prenom, email):
            return

        self.adherent_controller.add_adherent(nom, prenom, email)
        messagebox.showinfo("Succès", "Adhérent ajouté avec succès.")
        self.refresh_adherent_list()

    def rechercher_adherent(self):
        """Recherche des adhérents dans la base de données."""
        query = self.entry_nom.get()
        self.refresh_adherent_list(query)

    def refresh_adherent_list(self, query=""):
        """Rafraîchit la liste des adhérents affichée."""
        adherents = self.adherent_controller.search_adherents(query)
        self.text_results.delete(1.0, tk.END)
        for adherent in adherents:
            self.text_results.insert(tk.END, f"ID: {adherent[0]}, Nom: {adherent[1]}, Prénom: {adherent[2]}, Email: {adherent[3]}\n")
